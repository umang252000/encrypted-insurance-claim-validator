from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from app.auth import require_role
from app.similarity import (
    store_encrypted_vector,
    encrypted_similarity_search
)
from app.anomaly import cost_anomaly_score
from app.audit import record_audit, get_audit_log


app = FastAPI(
    title="Encrypted Insurance Claim Validator",
    description="Zero-knowledge fraud detection using encrypted embeddings",
    version="0.4"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for demo
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Models ----------

class EncryptedPayload(BaseModel):
    enc_blob: str
    nonce: str


class ValidationRequest(BaseModel):
    claim_id: str
    claimed_amount: float
    expected_amount: float
    claim_embedding: EncryptedPayload
    medical_embeddings: List[EncryptedPayload]


# ---------- Health ----------

@app.get("/health")
def health():
    return {
        "status": "ok",
        "encryption": "enabled",
        "fraud_engine": "enabled",
        "audit": "enabled"
    }


@app.options("/validate")
def options_validate():
    return {}

# ---------- Core Validation (RBAC: insurer only) ----------

@app.post("/validate")
def validate(
    req: ValidationRequest,
    token=Depends(require_role("insurer"))
):
    """
    End-to-end encrypted claim validation.
    No plaintext vectors are stored or processed.
    """

    for med in req.medical_embeddings:
        store_encrypted_vector("medical", med.dict())

    store_encrypted_vector("claims", req.claim_embedding.dict())

    similarity_score = encrypted_similarity_search(
        req.claim_embedding.dict()
    )

    cost_score = cost_anomaly_score(
        req.claimed_amount,
        req.expected_amount
    )

    fraud_risk = round(
        (0.6 * (1 - similarity_score)) +
        (0.4 * cost_score),
        2
    )

    # 🔐 Insurance-grade deterministic decision logic

    # 1️⃣ Extreme inflation → auto reject
    if cost_score >= 0.8:
        decision = "REJECT"
        fraud_risk = max(fraud_risk, 0.8)

    # 2️⃣ Moderate inflation → always manual review
    elif cost_score >= 0.4:
        decision = "MANUAL_REVIEW"
        fraud_risk = max(fraud_risk, 0.4)

    # 3️⃣ Normal AI-based decision
    elif fraud_risk < 0.3:
        decision = "APPROVE"

    elif fraud_risk < 0.7:
        decision = "MANUAL_REVIEW"

    else:
        decision = "REJECT"

    audit_event = {
        "claim_id": req.claim_id,
        "encrypted_similarity_score": similarity_score,
        "cost_anomaly_score": cost_score,
        "fraud_risk": fraud_risk,
        "decision": decision,
        "zero_knowledge": True
    }

    record_audit(audit_event)

    return audit_event


# ---------- Audit (RBAC: admin only) ----------

@app.get("/audit/logs")
def audit_logs(
    token=Depends(require_role("admin"))
):
    return get_audit_log()
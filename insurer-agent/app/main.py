from fastapi import FastAPI
from pydantic import BaseModel
from app.config import settings
from app.embedder import deterministic_embedding
from app.encrypt import encrypt_vector

app = FastAPI(
    title="Insurer Agent",
    description="Generates encrypted insurance claim embeddings",
    version="0.2"
)

class InsuranceClaim(BaseModel):
    claim_id: str
    procedure_code: str
    description: str
    claimed_amount: float

@app.get("/health")
def health():
    return {
        "service": settings.SERVICE_NAME,
        "status": "ok",
        "tenant": settings.TENANT_ID
    }

@app.post("/embed/claim")
def embed_claim(claim: InsuranceClaim):
    combined_text = f"""
    Procedure Code: {claim.procedure_code}
    Description: {claim.description}
    Amount: {claim.claimed_amount}
    """
    vector = deterministic_embedding(combined_text)
    encrypted = encrypt_vector(vector, settings.TENANT_ID)
    return {
        "claim_id": claim.claim_id,
        "encrypted_embedding": encrypted,
        "note": "Encrypted before leaving insurer boundary"
    }
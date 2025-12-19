from fastapi import FastAPI
from pydantic import BaseModel
from app.config import settings
from app.embedder import deterministic_embedding
from app.encrypt import encrypt_vector

app = FastAPI(
    title="Hospital Agent",
    description="Generates encrypted medical embeddings for insurance validation",
    version="0.2"
)

class MedicalRecord(BaseModel):
    patient_id: str
    diagnosis: str
    procedures: str
    notes: str

@app.get("/health")
def health():
    return {
        "service": settings.SERVICE_NAME,
        "status": "ok",
        "tenant": settings.TENANT_ID
    }

@app.post("/embed/medical")
def embed_medical(record: MedicalRecord):
    combined_text = f"""
    Diagnosis: {record.diagnosis}
    Procedures: {record.procedures}
    Notes: {record.notes}
    """
    vector = deterministic_embedding(combined_text)
    encrypted = encrypt_vector(vector, settings.TENANT_ID)
    return {
        "patient_id": record.patient_id,
        "encrypted_embedding": encrypted,
        "note": "Plaintext vector never stored or transmitted"
    }
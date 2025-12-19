import base64
import json
import hashlib

def encrypt_vector(vector: list, tenant_id: str) -> dict:
    payload = {
        "tenant": tenant_id,
        "vector_hash": hashlib.sha256(
            json.dumps(vector).encode()
        ).hexdigest()
    }

    encrypted_blob = base64.b64encode(
        json.dumps(payload).encode()
    ).decode()

    return {
        "enc_blob": encrypted_blob,
        "nonce": hashlib.md5(encrypted_blob.encode()).hexdigest()
    }
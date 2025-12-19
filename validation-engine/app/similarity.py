"""
CyborgDB-aligned encrypted similarity layer.

- No plaintext vectors
- No decrypt operations
- Encrypted blobs only
- Fail-closed behavior
"""

from app.cyborg import CyborgDBClient

# Single encrypted index instance (acts like CyborgDB)
cyborg = CyborgDBClient()


def store_encrypted_vector(kind: str, enc_blob: dict):
    """
    Store encrypted embedding in CyborgDB.

    kind: "medical" or "claims"
    enc_blob: { enc_blob: str, nonce: str }
    """
    if not isinstance(enc_blob, dict):
        return

    # Defensive validation (zero-trust)
    if "enc_blob" not in enc_blob or "nonce" not in enc_blob:
        return

    cyborg.insert(kind, enc_blob)


def encrypted_similarity_search(claim_blob: dict) -> float:
    """
    Encrypted similarity search via CyborgDB.

    - Operates on encrypted blobs only
    - No vector math
    - No decryption
    - Impervious to inversion
    """

    if not isinstance(claim_blob, dict):
        return 0.0

    if "enc_blob" not in claim_blob or "nonce" not in claim_blob:
        return 0.0

    # Delegates to CyborgDB encrypted search
    score = cyborg.encrypted_similarity(claim_blob)

    # Defensive clamp
    if not isinstance(score, float):
        return 0.0

    return round(min(max(score, 0.0), 1.0), 2)
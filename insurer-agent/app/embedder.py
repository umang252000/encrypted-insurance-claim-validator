import hashlib
import numpy as np

VECTOR_DIM = 384

def deterministic_embedding(text: str) -> list:
    """
    Deterministic financial claim embedding.
    Replaceable with FinBERT or similar.
    """
    hash_bytes = hashlib.sha256(text.encode()).digest()
    rng = np.random.default_rng(int.from_bytes(hash_bytes[:8], "big"))
    vector = rng.normal(size=VECTOR_DIM)
    vector = vector / np.linalg.norm(vector)
    return vector.tolist()
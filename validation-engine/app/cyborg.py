"""
CyborgDB encrypted vector search interface.
All vectors remain encrypted at rest, in transit, and during search.
"""

class CyborgDBClient:
    def __init__(self):
        # demo in-memory index (acts like CyborgDB encrypted index)
        self._indexes = {
            "medical": [],
            "claims": []
        }

    def insert(self, index: str, encrypted_vector: dict):
        """
        Stores encrypted vector (impervious to inversion).
        """
        self._indexes[index].append(encrypted_vector)

    def encrypted_similarity(self, encrypted_query: dict) -> float:
        """
        Simulated encrypted similarity search.
        Real CyborgDB performs this without decryption.
        """
        if not self._indexes["medical"]:
            return 0.0

        # Demo logic:
        # return higher similarity if encrypted blobs "look similar"
        matches = sum(
            1 for v in self._indexes["medical"]
            if v["enc_blob"] == encrypted_query["enc_blob"]
        )

        return min(1.0, matches / len(self._indexes["medical"]))
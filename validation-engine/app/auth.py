from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

SECRET_KEY = "demo-secret-key"
ALGORITHM = "HS256"

security = HTTPBearer()

def verify_token(
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return payload


def require_role(role: str):
    def role_dependency(payload=Depends(verify_token)):
        if payload.get("role") != role:
            raise HTTPException(
                status_code=403,
                detail="Forbidden"
            )
        return payload
    return role_dependency
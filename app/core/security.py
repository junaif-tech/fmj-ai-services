from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
import requests
from app.core.config import settings

bearer = HTTPBearer()
_jwks = None

def get_jwks():
    global _jwks
    if not _jwks:
        response = requests.get(settings.jwks_url)
        _jwks = response.json()
    return _jwks

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    token = credentials.credentials
    jwks = get_jwks()
    try:
        header = jwt.get_unverified_header(token)
        key = next(k for k in jwks["keys"] if k["kid"] == header["kid"])
        payload = jwt.decode(
            token,
            key,
            algorithms=key["alg"],
            audience=settings.api_audience,
            issuer=f"https://login.microsoftonline.com/{settings.azure_tenant}/v2.0"
        )
        return payload
    except (JWTError, StopIteration):
        raise HTTPException(status_code=401, detail="Invalid or expired token")

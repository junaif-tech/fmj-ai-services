from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import InputSchema, OutputSchema
from app.services.inference import predict
from app.core.security import verify_token

router = APIRouter()

@router.post("/predict", response_model=OutputSchema)
def ai_predict(payload: InputSchema, token_data=Depends(verify_token)):
    try:
        result = predict(payload.text)
        return OutputSchema(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

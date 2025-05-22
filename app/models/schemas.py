from pydantic import BaseModel

class InputSchema(BaseModel):
    text: str

class OutputSchema(BaseModel):
    result: str
    model: str = "stub"

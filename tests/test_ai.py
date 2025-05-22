import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_predict(monkeypatch):
    async def fake_verify_token(credentials):
        return {"sub": "test-user"}
    monkeypatch.setattr("app.core.security.verify_token", fake_verify_token)

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/v1/ai/predict", json={"text": "hello"})
        assert response.status_code == 200
        data = response.json()
        assert data["result"] == "Echo: hello"

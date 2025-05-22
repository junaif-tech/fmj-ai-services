# AI Service

This FastAPI microservice provides AI inference endpoints secured via Azure AD OAuth2 client-credentials flow.

## Setup

1. Copy `.env.example` to `.env` and fill in values.
2. Install dependencies or use Docker Compose.

## Running Locally

```bash
docker-compose up --build
```

## Testing

```bash
pytest
```

## GCP Deployment

```bash
# Push code to trigger Cloud Build:
gcloud builds submit --config cloudbuild.yaml .
```

## Django Integration

```python
from msal import ConfidentialClientApplication
import requests, os

msal_app = ConfidentialClientApplication(
    os.getenv("AZURE_DJANGO_CLIENT_ID"),
    authority=f"https://login.microsoftonline.com/{os.getenv('AZURE_TENANT')}",
    client_credential=os.getenv("AZURE_DJANGO_CLIENT_SECRET")
)

def call_ai(payload):
    token = msal_app.acquire_token_for_client([f"api://{os.getenv('AZURE_CLIENT_ID')}/.default"])
    headers = {"Authorization": f"Bearer {token['access_token']}"}
    return requests.post(os.getenv("AI_SERVICE_URL") + "/api/v1/ai/predict", json=payload, headers=headers).json()
```

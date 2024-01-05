from fastapi import FastAPI
from api_collections import feature_a_endpoints

app = FastAPI()

app.include_router(feature_a_endpoints.router, prefix="/feature_a", tags=["feature_a"])

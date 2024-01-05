from fastapi import FastAPI
from api_collections import feature_a_endpoints
from api_collections import feature_b_endpoints

app = FastAPI()

app.include_router(feature_a_endpoints.router, prefix="/feature_a", tags=["feature_a"])
app.include_router(feature_b_endpoints.router, prefix="/feature_b", tags=["feature_b"])

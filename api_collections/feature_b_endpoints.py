from fastapi import APIRouter
from api_collections.feature_b import FeatureB

router = APIRouter()
feature_a = FeatureB()

@router.get("/feature_b")
def get_status():
    return feature_a.get_status()
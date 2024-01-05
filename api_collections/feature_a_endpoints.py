from fastapi import APIRouter
from api_collections.feature_a import FeatureA

router = APIRouter()
feature_a = FeatureA()

@router.get("/feature_a")
def get_status():
    return feature_a.get_status()
from fastapi import FastAPI
from utils.logger import logger
from api.services import (
    get_analytics
)

from api.schemas import (
    HealthResponse,
    AnalyticsResponse
)
from fastapi import Header

API_KEY = "EmotionSense"

def validate_key(
    x_api_key: str = Header(...)
):

    if x_api_key != API_KEY:

        raise Exception(
            "Unauthorized"
        )
app = FastAPI(
    title="EmotionSense API"
)

# --------------------
# Health Check
# --------------------

@app.get(
    "/",
    response_model=HealthResponse
)
def home():

    return {
        "status":"running"
    }

# --------------------
# Analytics
# --------------------

@app.get(
    "/analytics",
    response_model=AnalyticsResponse
)
def analytics():

    return get_analytics()


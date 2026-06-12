from pydantic import BaseModel

class PredictionResponse(BaseModel):

    emotion: str
    confidence: float


class HealthResponse(BaseModel):

    status: str


class AnalyticsResponse(BaseModel):

    total_predictions: int
    average_confidence: float
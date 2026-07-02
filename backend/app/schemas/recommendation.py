from pydantic import BaseModel


class Recommendation(BaseModel):
    title: str
    summary: str
    rationale: str


class RecommendationResponse(BaseModel):
    recommendation: Recommendation

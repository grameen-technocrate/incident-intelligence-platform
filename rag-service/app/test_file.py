from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

req = QuestionRequest(
    question="Kafka"
)

print(req.__dict__)
print(req.model_dump())
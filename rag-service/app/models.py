from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str


# req = QuestionRequest(
#     question="What is Kafka ISR?"
# )

# print(req)
# print(type(req))
# print(req.question)
# print(type(req.question))

req = QuestionRequest(
    question="Kafka"
)

print(req.__dict__)
print(req.model_dump())
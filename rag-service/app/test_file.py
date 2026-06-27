from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    age: int

emp = Employee(
    name="Mintoo",
    age=30
)

print(emp)
print(emp.__dict__)
print(emp.model_dump())
print(emp.__annotations__)
# print(emp)
# print(emp.__dict__)
# print(emp.model_dump())
# print(Employee.__annotations__)
#test
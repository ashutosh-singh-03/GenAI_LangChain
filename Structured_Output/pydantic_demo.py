from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name: str = "Ashutosh"  # setting default value
    age: Optional[int] = None
    mail: EmailStr
    cgpa: float = Field(gt=5, lt=10, default=7, description="This tells about the cgpa of the student.")


new_student = {"name": "Ashutosh"}
new_student_2 = {"age": "32", "cgpa": 5}

student = Student(**new_student)
print(student)

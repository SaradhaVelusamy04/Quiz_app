from pydantic import BaseModel, Field
from typing import Optional, Dict

# User
class UserRegister(BaseModel):
    email: str
    password: str = Field(..., max_length=72)  # bcrypt limit

class UserLogin(BaseModel):
    email: str
    password: str = Field(..., max_length=72)

class UserCreate(UserRegister):
    pass

# Question
class QuestionCreate(BaseModel):
    question: str
    option1: str
    option2: str
    option3: str
    answer: Optional[str] = None  # correct answer

class QuestionSchema(BaseModel):
    id: int
    question: str
    option1: str
    option2: str
    option3: str
    answer: Optional[str] = None  # don’t expose to quiz takers

    class Config:
        orm_mode = True

# Quiz answers
class QuizAnswer(BaseModel):
    answers: Dict[int, str]  # {"question_id": "selected_option"}

# crud.py
from typing import Optional, List, Dict, Any, cast
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from passlib.hash import bcrypt
from typing import cast

from models import User, Question, Result
import schemas

# Passlib context (recommended)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ---------------- Users ----------------
def create_user(db: Session, user: schemas.UserRegister):
    from passlib.hash import bcrypt
    hashed_pw = bcrypt.hash(user.password[:72])
    db_user = User(email=user.email, hashed_password=hashed_pw)  # Use correct column name
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_user(db: Session, email: str, password: str) -> Optional[User]:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    # bcrypt.verify takes the actual string, not Column
    if not bcrypt.verify(password, str( user.hashed_password)):
        return None
    return user


# ---------------- Questions ----------------
def create_question(db: Session, question: schemas.QuestionCreate) -> Question:
    """
    Create and return a Question DB object.
    """
    db_q = Question(
        question=question.question,
        option1=question.option1,
        option2=question.option2,
        option3=question.option3,
        answer=question.answer,
    )
    db.add(db_q)
    db.commit()
    db.refresh(db_q)
    return db_q


def get_all_questions(db: Session) -> List[Question]:
    """
    Return all questions (ORM objects).
    """
    return db.query(Question).all()


def get_question(db: Session, qid: int) -> Optional[Question]:
    return db.query(Question).filter(Question.id == qid).first()


def delete_question(db: Session, qid: int) -> bool:
    q = db.query(Question).filter(Question.id == qid).first()
    if q:
        db.delete(q)
        db.commit()
        return True
    return False


# ---------------- Results ----------------
def save_result(db: Session, user_id: int, score: int) -> Result:
    """
    Save a Result row for the user and return it.
    """
    res = Result(user_id=user_id, score=score)
    db.add(res)
    db.commit()
    db.refresh(res)
    return res


def get_user_results(db: Session, user_id: int) -> List[Result]:
    return db.query(Result).filter(Result.user_id == user_id).all()

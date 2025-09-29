from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal
from models import Base


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Register user
@app.post("/register")
def register(user: schemas.UserRegister, db: Session = Depends(get_db)):
    try:
        return crud.create_user(db, user)
    except Exception as e:
        print(e)  # Will show in terminal
        return {"error": str(e)}

# Login user
@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.verify_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": db_user.id}

# Add question
@app.post("/questions")
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
       return crud.create_question(db=db, question=question)

# Get questions (don’t show correct answers)
@app.get("/questions", response_model=list[schemas.QuestionSchema])
def get_questions(db: Session = Depends(get_db)):
    return crud.get_all_questions(db)

# Save quiz result
@app.post("/results")
def save_result(user_id: int, score: int, db: Session = Depends(get_db)):
    result = crud.save_result(db, user_id, score)
    return {"id": result.id, "score": result.score}

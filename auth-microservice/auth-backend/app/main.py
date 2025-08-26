from fastapi import FastAPI, Depends
from .auth import get_current_user
from .database import Base, engine, SessionLocal
from .models import User
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or ["*"] for all origins (dev only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/auth/verify-token")
def verify_token(user=Depends(get_current_user)):
    auth0_id = user["sub"]
    email = user.get("email")
    first_name = user.get("given_name")
    last_name = user.get("family_name")
    db = SessionLocal()
    db_user = db.query(User).filter(User.auth0_id == auth0_id).first()
    if not db_user:
        db_user = User(
            auth0_id=auth0_id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            status="active"
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    return {
        "id": db_user.id,
        "auth0_id": db_user.auth0_id,
        "email": db_user.email,
        "first_name": db_user.first_name,
        "last_name": db_user.last_name,
        "is_active": db_user.is_active,
        "status": db_user.status
    }
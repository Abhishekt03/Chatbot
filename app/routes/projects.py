from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import models, schemas
from app.auth import get_current_user
from app.database import get_db


router = APIRouter(prefix="/projects", tags=["Projects"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ProjectResponse)
def create_project(
    project: schemas.ProjectCreate,
    db: Session = Depends(get_db),
    email: str = Depends(get_current_user)
):
    user = db.query(models.User).filter(
        models.User.email == email
    ).first()

    new_project = models.Project(
        name=project.name,
        user_id=user.id
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project

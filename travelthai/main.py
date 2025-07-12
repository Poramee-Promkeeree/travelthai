from fastapi import FastAPI
from .auth import auth_router
from .database import Base, engine
from . import models
from .router.travel import router as travel_router
from .model.travel import seed_provinces

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(travel_router, prefix="/travel", tags=["travel"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.on_event("startup")
def startup_event():
    from .database import SessionLocal
    db = SessionLocal()
    seed_provinces(db)
    db.close()
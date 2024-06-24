from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from . import models, schemas, crud
from .database import SessionLocal, engine
from fastapi.responses import RedirectResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_tasks(request: Request, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db)
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.get("/tasks/create")
def create_task_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/tasks/create")
def create_task(request: Request, db: Session = Depends(get_db), title: str = Form(...), description: str = Form(None)):
    task = schemas.TaskCreate(title=title, description=description)
    crud.create_task(db, task)
    return RedirectResponse("/", status_code=303)

@app.get("/tasks/{task_id}")
def read_task(task_id: int, request: Request, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return templates.TemplateResponse("update.html", {"request": request, "task": task})

@app.post("/tasks/{task_id}")
def update_task(task_id: int, request: Request, db: Session = Depends(get_db), title: str = Form(...), description: str = Form(None), done: bool = Form(False)):
    task = schemas.TaskUpdate(title=title, description=description, done=done)
    updated_task = crud.update_task(db, task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return RedirectResponse("/", status_code=303)

@app.post("/tasks/{task_id}/delete")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    crud.delete_task(db, task_id)
    return RedirectResponse("/", status_code=303)

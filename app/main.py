from fastapi import FastAPI

from app.routes import router


app = FastAPI(
    title="Task API",
    description="API para gerenciamento de tarefas",
    version="1.0.0",
)


@app.get("/", tags=["Health"])
def home():
    return {"message": "Task API funcionando"}


app.include_router(router)
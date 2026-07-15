from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=500)
    completed: bool = False


class TaskResponse(TaskCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
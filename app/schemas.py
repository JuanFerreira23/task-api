from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=500)
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
    )
    description: str | None = Field(
        default=None,
        min_length=3,
        max_length=500,
    )
    completed: bool | None = None


class TaskResponse(TaskCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
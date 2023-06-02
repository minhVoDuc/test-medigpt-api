from pydantic import BaseModel

class GptMsg(BaseModel):
    user_id: int
    content: str | None = None
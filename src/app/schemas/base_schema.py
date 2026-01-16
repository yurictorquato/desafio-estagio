from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        extra="forbid", from_attributes=True, str_strip_whitespace=True
    )

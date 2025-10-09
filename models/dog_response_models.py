from pydantic import BaseModel, Field, HttpUrl


class DogApiBaseResponse(BaseModel):
    status: str = Field(..., pattern="success")


class ListAllBreedsResponse(DogApiBaseResponse):
    message: dict[str, list[str]]


class ImagesResponse(DogApiBaseResponse):
    message: list[HttpUrl]


class RandomImageResponse(DogApiBaseResponse):
    message: HttpUrl


class SubBreedsListResponse(DogApiBaseResponse):
    message: list[str]


class ErrorResponse(BaseModel):
    status: str = Field(..., pattern="error")
    message: str
    code: int

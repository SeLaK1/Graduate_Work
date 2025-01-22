from pydantic import BaseModel


class CreateCategory(BaseModel):
    name: str
    parent_id: int

class CreateProduct(BaseModel):
    name: str
    description: str
    price: int
    image_url: str
    stock: int
    category: int


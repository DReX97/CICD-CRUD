from decimal import Decimal
from pydantic import BaseModel, Field

# Base schema with common attributes
# class ItemBase(BaseModel):
#     name: str
#     description: str = None


class ItemBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    description: str | None = Field(default=None, min_length=2, max_length=200)
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)  # Price must be greater than 0 and have up to 10 digits with 2 decimal places

# Schema for creating a new item
class ItemCreate(ItemBase):
    pass


# Schema for reading/returning an item (includes id)
class Item(ItemBase):
    id: int

    class Config:
        from_attributes = True

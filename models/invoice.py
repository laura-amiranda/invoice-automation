from pydantic import BaseModel
from models.item import Item


class Invoice(BaseModel):
    order_id: int
    customer_id: str
    order_date: str
    items: list[Item]
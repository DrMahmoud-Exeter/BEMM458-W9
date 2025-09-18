from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Product:
    product_id: str
    category: str
    price: float

@dataclass
class User:
    username: str
    segment: str = "new"
    active: bool = True
    purchases: Dict[str, int] = field(default_factory=dict)

    def add_purchase(self, product_id: str, qty: int = 1):
        self.purchases[product_id] = self.purchases.get(product_id, 0) + qty

    def total_items(self) -> int:
        return sum(self.purchases.values())

    def __str__(self) -> str:
        return f"User(username={self.username}, segment={self.segment}, active={self.active}, items={self.total_items()})"

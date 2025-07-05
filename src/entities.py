from dataclasses import dataclass
from src.enums import ProductCategory


@dataclass
class Product:
    name: str
    unit_price: int
    category: ProductCategory = ProductCategory.DEFAULT


@dataclass
class OrderItem:
    product: Product
    quantity: int


@dataclass
class Order:
    items: list[OrderItem]
    total_amount: int = 0
    original_amount: int = 0
    discount: int = 0

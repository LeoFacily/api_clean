from dataclasses import dataclass

@dataclass
class ProductDTO:
    description: str
    price: float
    technical_details: str
    image: str
    visible: bool
    category_id: int
    supplier_id: int
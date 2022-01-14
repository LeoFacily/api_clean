from pydantic import BaseModel

class CreateSupplierSchema(BaseModel):
    name: str
from dataclasses import dataclass

@dataclass
class AddressDTO:
    address: str
    primary: str
    customer_id: int
from email.headerregistry import Address
from typing import List

class Customer:
    
    def __init__(self, first_name: str, last_name: str, address: list[Address] = []) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.address: List[Address] = []

    def add_address(self, address: Address):
        if address.primary:
            filter_primary = list(filter(lambda x: x.primary == True, self.address))

            if len(filter_primary) > 0:
                filter_primary[0].primary = False

        self.address.append(address)


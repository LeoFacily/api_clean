class Address:
    def __init__(self, address: str, primary: bool, customer_id: int) -> None:
        self.address = address
        self.primary = primary
        self.customer_id = customer_id
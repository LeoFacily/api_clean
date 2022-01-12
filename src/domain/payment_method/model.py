from typing import Any, Optional


class PaymentMethod:
    def __init__(self, name: str, enabled: bool, id: Optional[int] = None):
        self.id = id
        self.name = name
        self.enabled = enabled

from datetime import datetime


class Coupon:
    def __init__(self, code: str, limit: int, expire_at: datetime, mode: str, value: float) -> None:
        self.code = code
        self.limit = limit
        self.expire_at = expire_at
        self.mode = mode
        self.value = value

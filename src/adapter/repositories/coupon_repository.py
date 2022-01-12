from src.domain.coupon.model import Coupon
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class CouponRepository(SqlAlchemyRepository[Coupon]):
  pass
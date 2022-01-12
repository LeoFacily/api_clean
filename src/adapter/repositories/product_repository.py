from src.domain.product.model import Product
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class ProductRepository(SqlAlchemyRepository[Product]):
  pass
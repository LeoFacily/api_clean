from src.domain.category.model import Category
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class CategoryRepository(SqlAlchemyRepository[Category]):
  pass
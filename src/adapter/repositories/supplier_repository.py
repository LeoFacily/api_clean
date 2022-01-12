from src.domain.supplier.model import Supplier
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class SupplierRepository(SqlAlchemyRepository[Supplier]):
  pass
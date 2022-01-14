from src.domain.customer.model import Customer
from src.adapter.sqlalchemy_repository import SqlAlchemyRepository


class CustomerRepository(SqlAlchemyRepository[Customer]):
  pass
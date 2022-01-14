from src.domain.supplier.model import Supplier
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork


def create_supplier(name, uow: SqlAlchemyUnitOfWork):
    with uow:
        uow.supplier_repository.add(Supplier(name=name))

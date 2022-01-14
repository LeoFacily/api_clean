from src.domain.supplier.model import Supplier
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.supplier.supplier_dto import SupplierDTO 


def create_supplier(supplier_dto: SupplierDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        uow.supplier_repository.add(Supplier(name=supplier_dto.name))
        uow.commit()
from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.supplier_schema import CreateSupplierSchema
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.supplier.supplier_dto import SupplierDTO
from src.services.supplier.supplier_service import create_supplier

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(schema: CreateSupplierSchema):
    uow = SqlAlchemyUnitOfWork()
    dto = SupplierDTO(**schema.dict())
    supplier = create_supplier(dto, uow=uow)

    return 
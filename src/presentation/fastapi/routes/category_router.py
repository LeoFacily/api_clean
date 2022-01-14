from fastapi import APIRouter, status
from src.presentation.fastapi.schemas.category_schema import CreateCategorySchema
from src.services.category.category_dto import CategoryDTO
from src.services.category.category_service import create_category
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(schema: CreateCategorySchema):
  uow = SqlAlchemyUnitOfWork()
  dto = CategoryDTO(**schema.dict())
  
  category = create_category(dto, uow=uow)

  return category
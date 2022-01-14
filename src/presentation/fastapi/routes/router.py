from fastapi import APIRouter
from src.presentation.fastapi.routes.product_router import router as product_router
from src.presentation.fastapi.routes.category_router import router as category_router
from src.presentation.fastapi.routes.supplier_router import router as supplier_router

router = APIRouter()

router.include_router(product_router, prefix='/products', tags=['product'])
router.include_router(category_router, prefix='/category' tags=['category'])
router.include_router(supplier_router, prefix='/supplier' tags=['supplier'])


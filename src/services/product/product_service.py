from src.domain.product.model import Product
from src.domain.product_discount.model import ProductDiscount
from src.services.product.product_dto import ProductDTO
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

def create_product(product_dto: ProductDTO, uow: SqlAlchemyUnitOfWork):
  with uow:
    category = uow.category_repository.get(id = product_dto.category_id)

    if not category:
      raise Exception('Category not found')

    supplier = uow.supplier_repository.get(id = product_dto.supplier_id)

    if not supplier:
      raise Exception('Supplier not found')
    

    product = Product(
      description = product_dto.description, 
      price = product_dto.price, 
      technical_details = product_dto.technical_details,
      image = product_dto.image,
      visible = product_dto.visible,
      category = category,
      supplier = supplier)

    uow.product_repository.add(product)

    uow.commit()

    return product
  

def create_discount(mode: str, value: float, payment_method_id: int, product_id: int, uow: SqlAlchemyUnitOfWork):
  with uow:
    product = uow.product_repository.get(id=product_id)

    if not product:
      raise Exception('Product not found')

    payment_method = uow.payment_method_repository.get(id=payment_method_id)

    if not payment_method:
      raise Exception('Payment method not found')


    discount = ProductDiscount(mode=mode, value=value, payment_method=payment_method)
    product.add_discount(discount)

    uow.commit()

from src.domain.product.model import Product
from src.domain.product_discount.model import ProductDiscount
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

def create_product(description: str, price: float, technical_details: str, image: str, visible: bool, category_id: int, supplier_id: int, uow: SqlAlchemyUnitOfWork):
  with uow:
    category = uow.category_repository.get(id=category_id)

    if not category:
      raise Exception('Category not found')

    supplier = uow.supplier_repository.get(id=supplier_id)

    if not supplier:
      raise Exception('Supplier not found')
    

    product = Product(description=description, price=price, technical_details=technical_details, image=image, visible=visible, category=category, supplier=supplier)

    uow.product_repository.add(product)

    uow.commit()
  

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

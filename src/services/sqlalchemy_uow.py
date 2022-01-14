from src.adapter.repositories.category_repository import CategoryRepository
from src.adapter.repositories.payment_method_repository import PaymentMethodRepository
from src.adapter.repositories.supplier_repository import SupplierRepository
from src.adapter.repositories.product_repository import ProductRepository
from src.adapter.repositories.customer_repository import CustomerRepository
from src.adapter.repositories.address_repository import AddressRepository
from src.domain.category.model import Category
from src.domain.customer.model import Customer
from src.domain.supplier.model import Supplier
from src.domain.payment_method.model import PaymentMethod
from src.domain.product.model import Product
from src.adapter.database import Session


class SqlAlchemyUnitOfWork:
  def __init__(self):
      self.session = Session


  def __enter__(self):
    self.payment_method_repository = PaymentMethodRepository(self.session, PaymentMethod)
    self.category_repository = CategoryRepository(self.session, Category)
    self.supplier_repository = SupplierRepository(self.session, Supplier)
    self.product_repository = ProductRepository(self.session, Product)
    self.customer_repository = CustomerRepository(self.session, Customer)
    self.address_repository = AddressRepository(self.session, AddressRepository)
    

  def __exit__(self, *args):
    self.session.rollback()
    self.session.close()

  def commit(self):
    self.session.commit()
from src.domain.address.model import Address 
from src.domain.customer import Customer
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork

def create_customer(first_name: str, last_name: str, uow: SqlAlchemyUnitOfWork):
    with uow:
        customer = Customer(first_name= first_name, last_name = last_name)

        uow.customer_repository.add(Customer)
        uow.commit()

def create_address(adress: str, primary: bool, uow: SqlAlchemyUnitOfWork):
    with uow:

        customer = uow.customer_repository.get(id=customer_id)
        address = Address(address=adress, primary = primary, uow=uow)
        customer.add_address(address)

        uow.commit()
from xml.dom import NotFoundErr
from src.domain.address.model import Address 
from src.domain.customer import Customer
from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.customer.customer_dto import CustomerDTO 
from src.services.address.address_dto import AddressDTO

def create_customer(customer_dto: CustomerDTO, uow: SqlAlchemyUnitOfWork):
    with uow:
        customer = Customer(
            first_name= customer_dto.first_name, 
            last_name = customer_dto.last_name)

        uow.customer_repository.add(Customer)
        uow.commit()

def create_address(address_dto: AddressDTO, uow: SqlAlchemyUnitOfWork):
    with uow:

        customer = uow.customer_repository.get(id= AddressDTO.customer_id)

        if not Customer:
            raise NotFoundErr('Customer Not Foun')

        address = Address(
            address = address_dto.address, 
            primary = address_dto.primary, 
            customer_id = address_dto.customer_id,
            uow = uow)
        customer.add_address(address)

        uow.commit()
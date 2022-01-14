from src.services.sqlalchemy_uow import SqlAlchemyUnitOfWork
from src.services.category_service import create_category
from src.adapter.database import Session
from src.adapter.orm import start_mapper


start_mapper()

db = Session()

uow = SqlAlchemyUnitOfWork(db)

create_category('Categoria 1', uow)




# with uow:
#   pm = PaymentMethod(name='pix', enabled=True, id=1)
#   uow.payment_method_repository.add(pm)


#   c = Category(name='eletronico')
#   uow.category_repository.add(c)
#   s = Supplier(name='HP')
#   uow.supplier_repository.add(s)


#   p = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True, category=c, supplier=s)
#   pd = ProductDiscount(mode='value', value=100, payment_method=pm)
#   p.add_discount(pd)

#   uow.product_repository.add(p)

#   print(len(p.discounts))

#   pm2 = PaymentMethod(name='boleto', enabled=True, id=2)
#   uow.payment_method_repository.add(pm2)

#   # pd2 = ProductDiscount(mode='percetage', value=100, payment_method=pm2)
#   # p.add_discount(pd2)


# payment_method_repository = PaymentMethodRepository(db, PaymentMethod)
# category_repository = CategoryRepository(db, Category)
# supplier_repository = SupplierRepository(db, Supplier)
# product_repository = ProductRepository(db, Product)


# ================= 
# Populando o banco de dados





# Adicionando um novo desconto

# p = db.query(Product).filter_by(id=1).first()

# # pm = db.query(PaymentMethod).filter_by(id=1).first()
# pm = PaymentMethod('cartão de crédito', enabled=True, id=3)

# pd = ProductDiscount(mode='value', value=100, payment_method=pm)

# print(len(p.discounts))


# p.add_discount(pd)

# print(p.id)
# db.commit()
# db.close()


# Buscando um desconto no banco de dados

# pd = db.query(ProductDiscount).filter_by(id=1).first()

# print(pd.value)
# print(pd.payment_method.name)



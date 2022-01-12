from src.domain.category.model import Category
from src.domain.supplier.model import Supplier
from src.adapter.database import Session
from src.adapter.orm import start_mapper
from src.domain.product_discount.model import ProductDiscount
from src.domain.payment_method.model import PaymentMethod
from src.domain.product.model import Product

start_mapper()

db = Session()

# ================= 
# Populando o banco de dados


# pm = PaymentMethod(name='pix', enabled=True, id=1)
# db.add(pm)
# pd = ProductDiscount(mode='value', value=100, payment_method=pm)
# db.add(pd)

# c = Category(name='eletronico')
# db.add(c)
# s = Supplier(name='HP')
# db.add(s)

# p = Product(description='descricao 2', price=10, technical_details='detalhes tecnicos', image='', visible=True, category=c, supplier=s)
# db.add(p)
# p.add_discount(pd)

# print(len(p.discounts))

# pm2 = PaymentMethod(name='boleto', enabled=True, id=2)
# db.add(pm2)
# pd2 = ProductDiscount(mode='percetage', value=100, payment_method=pm2)
# db.add(pd2)

# p.add_discount(pd2)

# db.commit()
# db.close()


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

pd = db.query(ProductDiscount).filter_by(id=1).first()

print(pd.value)
print(pd.payment_method.name)

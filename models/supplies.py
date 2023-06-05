from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base


class Supplies(Base):

    __tablename__ ="supplies"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    supplier_id = Column(Integer, ForeignKey("Supplier.id"))
    purchase_price = Column(Integer)
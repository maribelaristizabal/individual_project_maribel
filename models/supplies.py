from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base


class Supplies(Base):

    __tablename__ ="supplies"

    id = Column(Integer, primary_key=True)
    Supplier_ID = Column(Integer, ForeignKey("Supplier.ID"))
    Product_ID = Column(Integer, ForeignKey("Product.ID"))
    Pruchase_Price = Column(Integer)

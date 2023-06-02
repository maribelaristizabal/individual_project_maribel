from sqlalchemy import Column, Integer, String

from config.database import Base


class Product(Base):

    __tablename__="products"

    id = Column(Integer,primary_key=True)
    Name = Column(String)
    Brand = Column(String)
    Description = Column(String)
    Price = Column(Integer)
    Entry_date = Column(String)
    availability = Column(String)
    Avaliable_Quantity= Column(Integer)
    
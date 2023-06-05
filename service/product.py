from models.product import Product as ProductModel
from schemas.product import Product
class ProductService():
    def __init__(self, db):
        self.db = db
        
    def get_product(self):
        result = self.db.query(ProductModel).all()
        return result
    
    def  create_product(self,product:ProductModel):
        new_product = ProductModel(
            name = product.name.upper(),
            brand = product.brand.upper(),
            description = product.description.upper(),
            price = product.price,
            availability = product.availability.upper(),
            availiable_quantity = product.availiable_quantity
        )
        self.db.add(new_product)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id). first()
        return result
    
    def update_product(self,data:Product):
        product = self.db.query(ProductModel).filter(ProductModel.id ==data.id).first()
        product.name = data.name
        product.brand = data.brand
        product.description = data.description
        product.price = data.price
        product.availability= data.availability
        product.availiable_quantity = data.availiable_quantity


        self.db.commit()
        return
    
    def delete_product(self,id:int):
        self.db.query(ProductModel).filter(ProductModel.id == id).delete()
        self.db.commit()
        return       

        
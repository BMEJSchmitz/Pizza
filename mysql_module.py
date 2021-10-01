from pathlib import Path
from app import app
from flask_sqlalchemy import SQLAlchemy

Path("db").mkdir(parents=True, exist_ok=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/my_app.db"
db = SQLAlchemy(app)

class Customer(db.model):
    customer_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    phone_number = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(30))
    address = db.Column(db.String(30), unique=True)
    district_code = db.Column(db.String(6))
    city = db.Column(db.String(20))
    
    def CreateCustomer(phone, name, address, district, city):
        customer = Customer(phone_number=phone, name=name, address=address, district_code=district, city=city)
        db.session.add(customer)
        db.session.commit()
        
        return customer
    
    def FindCustomer(address, district, city):
        return Customer.query.filter_by(address=address, district_code=district, city=city).first()
    
class Order(db.model):
    order_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    customer_id = db.Column(db.Integer)
    discount_code = db.Column(db.String(10), unique=True)
    delivery_time = db.Column(db.Datetime)
    status = db.Column(db.String(20))
    
    #def CreateOrder():
        
        
    def FindOrder(order):
        return Order.query.filter_by(order_id=order).first()
    
    
class DeliveryPerson(db.model):
    employee_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(30))
    area_code = db.Column(db.String(6))
    
    def CreateDeliveryPerson(employee_id, name, area):
        delivery_person = DeliveryPerson(employee_id, name, area)
        db.session.add(delivery_person)
        db.session.commit()
        
        return delivery_person
        
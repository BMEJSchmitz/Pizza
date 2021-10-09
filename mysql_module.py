from pathlib import Path
from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import timedelta

Path("db").mkdir(parents=True, exist_ok=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/my_app.db"
db = SQLAlchemy(app)

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    
    def FindCustomer(**kwargs):
        return Customer.query.filter_by(**kwargs).first()
    
    def __repr__(self):
        return f"Customer {self.customer_id}, {self.name}, {self.phone_number}, {self.address}, {self.area_code}, {self.city}"

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    discount_code = db.Column(db.String(10), unique=True)
    delivery_time = db.Column(db.DateTime)
    status = db.Column(db.String(20))
    
    def CreateOrder(customer, discount, items):
        time = datetime.now()
        order = Order(customer_id=customer, discount_code=discount, delivery_time=time + timedelta(mins = 15), status='In Process')
        
        for item in items:
            Order_Item.CreateOrderItem(order_id=order.order_id, item=item, quantity=items[item])
            
        db.session.add(order)
        db.session.commit()
           
        return order
           
        
    def FindOrder(**kwargs):
        return Order.query.filter_by(**kwargs).first()
    
    def CancelOrder(order):
        order.status = 'Cancelled'
        
        db.session.commit()
        
        return order
    
    def __repr__(self):
        ordered = Order_Item.query.filter(order_id=self.order_id)
        items = ", ".join(ordered)
        return f"Order {self.order_id}, {self.delivery_time}, {self.status}, "+items
    
class Order_Item(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), primary_key=True)
    item = db.Column(db.String(30), primary_key=True)
    quantity = db.Column(db.Integer)
    
    def CreateOrderItem(order_id, item, quantity):
        order_item = Order_Item(order_id=order_id, item=item, quantity=quantity)
        
        db.session.add(order_item)
        db.session.commit()
        
        return order_item
    
    def __repr__(self):
        return f"Item {self.item}, amount {self.quantity}"
        
class DeliveryPerson(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    area_code = db.Column(db.String(6))
    
    def CreateDeliveryPerson(employee_id, name, area):
        delivery_person = DeliveryPerson(employee_id, name, area)
        db.session.add(delivery_person)
        db.session.commit()
        
        return delivery_person
    
    def __repr__(self):
        return f"Delivery Person {self.employee_id}, {self.name}, {self.area_code}"
        
db.create_all()
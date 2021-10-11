# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pathlib import Path
from app import app
from flask_sqlachemy import SQLAlchemy
from datetime import datetime
from datetime import timedelta

Path("db").mkdir(parents = True, exist_ok=True)
app.config["Pizza API"] = "sqlite:///db/pizza.db"
db = SQLAlchemy(app)

class Pizza(db.Model):
    pizza_id = db.Column(db.Integer(5), primary_key = True, auto_increment= True)
    name = db.Column(db.String(30), nullable = False)
    toppings_id = db.Column(db.Integer(3), primary_key=True, nullable=False)
    
    def create_pizza(self, name,toppings_id):
        pizza = []
        for topping in toppings_id:
            row = Pizza(name,topping)
            pizza.append(row)
        return pizza
    
     #adding pizzas to database   
    def rows(self):
        pizza_1 = self.create_pizza('New Haven Style', [1,2,3,4,5])
        db.session.add(pizza_1)
        pizza_2 = self.create_pizza('St.Louis Style', [2,3,4,5,6])
        db.session.add(pizza_2)
        pizza_3 = self.create_pizza('Neapolitan', [3,4,5,6,7])
        db.session.add(pizza_3)
        pizza_4 = self.create_pizza('New York Style', [4,5,6,7,8])
        db.session.add(pizza_4)
        pizza_5 = self.create_pizza('Double Dough', [5,6,7,8,9])
        db.session.add(pizza_5)
        pizza_6 = self.create_pizza('Sicilian Style', [6,7,8,9,10])
        db.session.add(pizza_6)
        pizza_7 = self.create_pizza('Chicago Deep-Dish', [1,7,8,9,10,])
        db.session.add(pizza_7)
        pizza_8 = self.create_pizza('Focaccia', [1,2,8,9,10])
        db.session.add(pizza_8)
        pizza_9 = self.create_pizza('Gluten Free', [1,2,3,9,10])
        db.session.add(pizza_9)
        pizza_10 = self.create_pizza('Vegan Friendly', [1,2,3,4,10])
        db.session.add(pizza_10)
        db.session.commit()
    
    def __repr__(self):
        return f"Pizza {self.pizza_id}, {self.name}, {self.toppings_id}"
    
    def find_pizza(self,pizzaId):
        return Pizza.query.filter_by(pizza_id = pizzaId).first() 
    
    def get_pizzas(self,pizzaId):
        return Pizza.query.filter_by(pizza_id = pizzaId).all()
        
    
class Toppings(db.Model):
    toppings_id = db.Column(db.Integer(3), primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable = False)
    price = db.Coumn(db.Double(5), unique=True, nullable=False)
    vegetarian = db.Column(db.bool, nullable = False)
    
    def rows1(self):
        toppings_1 = Toppings(toppings_id = 1, name = 'Pepperoni', price = 5.99, vegetarian = False)
        db.session.add(toppings_1)
        toppings_2 = Toppings(toppings_id = 2, name = 'Mushroom', price = 3.99, vegetarian = True)
        db.session.add(toppings_2)
        toppings_3 = Toppings(toppings_id = 3, name = 'Extra Cheese', price = 4.99, vegetarian = True)
        db.session.add(toppings_3)
        toppings_4 = Toppings(toppings_id = 4, name = 'Sausage', price = 5.99, vegetarian = False)
        db.session.add(toppings_4)
        toppings_5 = Toppings(toppings_id = 5, name = 'Onion', price = 2.99, vegetarian = True)
        db.session.add(toppings_5)
        toppings_6 = Toppings(toppings_id = 6, name = 'Black Olives', price = 3.99, vegetarian = True)
        db.session.add(toppings_6)
        toppings_7 = Toppings(toppings_id = 7, name = 'Green Pepper', price = 3.99, vegetarian = True)
        db.session.add(toppings_7)
        toppings_8 = Toppings(toppings_id = 8, name = 'Fresh Garlic', price = 2.99, vegetarian = True)
        db.session.add(toppings_8)
        toppings_9 = Toppings(toppings_id = 9, name = 'Chicken', price = 6.99, vegetarian = False)
        db.session.add(toppings_9)
        toppings_10 = Toppings(toppings_id = 10, name = 'Tomato', price = 1.99, vegetarian = True)
        db.session.add(toppings_10)
        db.session.commit()
        
    def __repr__(self):
        return f"Toppings {self.toppings_id},{self.name},{self.price},{self.vegetarian}"
    
    def find_toppings(self,toppings_id):
        return Toppings.query.filter_by(toppings_id).first()
        
class drinks(db.Model):
    name = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Integer(5),nullable=False)
    
    def rows2(self):
        drink_1 = drinks(name= 'Coke', price = 1.99)
        db.session.add(drink_1)
        drink_2 = drinks(name= 'Iced Tea', price = 2.5)
        db.session.add(drink_2)
        drink_3 = drinks(name= 'Sprite', price = 1.99)
        db.session.add(drink_3)
        drink_4 = drinks(name= 'Beer', price = 1.99)
        db.session.add(drink_4)
        db.session.commit()
    
    def __repr__(self):
        return f"drinks {self.name}, {self.price}"
    
    def find_drinks(self,name):
        return drinks.query.filter_by(name).first()
    
    def get_drinks(self,name):
        return drinks.query.filter_by(name).all()
    
class desserts(db.Model):
    name = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Integer(5),nullable=False)
    
    def rows3(self):
        dessert_1 = desserts(name = 'Choco Lava Cake', price = 3.99)
        db.session.add(dessert_1)
        dessert_2 = desserts(name = 'Ice Cream', price = 2.5)
        db.session.add(dessert_2)
        db.session.add()
        
    def __repr__(self):
        return f"desserts {self.name}, {self.price}"
    
    def find_desserts(name):
        return desserts.query.filter_by(name).first()
    
    def get_desserts(self,name):
        return desserts.query.filter_by(name).all()
    
class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(30))
    address = db.Column(db.String(30), unique=True)
    district_code = db.Column(db.String(6))
    city = db.Column(db.String(20))
    
    def CreateCustomer(self, phone, name, address, district, city):
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
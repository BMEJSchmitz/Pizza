# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from pathlib import Path
from app import app
from flask_sqlachemy import SQLAlchemy

Path("db").mkdir(parents = True, exist_ok=True)
app.config["Pizza API"] = "sqlite:///db/pizza.db"
db = SQLAlchemy(app)

class Pizza(db.Model):
    pizza_id = db.Column(db.Integer(5), primary_key = True, auto_increment= True)
    name = db.Column(db.String(30), nullable = False)
    toppings_id = db.Column(db.Integer(3), primary_key=True, nullable=False)
    
    def create_pizza(name,toppings_id):
        pizza = []
        for topping in toppings_id:
            row = Pizza(name,topping)
            pizza.append(row)
        return pizza
    
        
    def rows(self):
        pizza_1 = create_pizza('New Haven Style', [1,2,3,4,5])
        db.session.add(pizza_1)
        pizza_2 = create_pizza('St.Louis Style', [2,3,4,5,6])
        db.session.add(pizza_2)
        pizza_3 = create_pizza('Neapolitan', [3,4,5,6,7])
        db.session.add(pizza_3)
        pizza_4 = create_pizza('New York Style', [4,5,6,7,8])
        db.session.add(pizza_4)
        pizza_5 = create_pizza('Double Dough', [5,6,7,8,9])
        db.session.add(pizza_5)
        pizza_6 = create_pizza('Sicilian Style', [6,7,8,9,10])
        db.session.add(pizza_6)
        pizza_7 = create_pizza('Chicago Deep-Dish', [1,7,8,9,10,])
        db.session.add(pizza_7)
        pizza_8 = create_pizza('Focaccia', [1,2,8,9,10])
        db.session.add(pizza_8)
        pizza_9 = create_pizza('Gluten Free', [1,2,3,9,10])
        db.session.add(pizza_9)
        pizza_10 = create_pizza('Vegan Friendly', [1,2,3,4,10])
        db.session.add(pizza_10)
        db.session.commit()
    
    
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
    
class desserts(db.Model):
    name = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Integer(5),nullable=False)
    
    def rows3(self):
        dessert_1 = desserts(name = 'Choco Lava Cake', price = 3.99)
        db.session.add(dessert_1)
        dessert_2 = desserts(name = 'Ice Cream', price = 2.5)
        db.session.add(dessert_2)
        db.session.add()
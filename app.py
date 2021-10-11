# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:36:02 2021

@author: Aditi Mishra
"""

from flask import Flask, make_response, request, render_template
app = Flask(__name__)
from model import Pizza, Toppings, drinks, desserts, Customer, Order

@app.route("/Pizza/<pizza_id>")
def get_Pizza(pizza_id: int):
    pizza = Pizza.find_pizza(pizza_id = pizza_id)
    if pizza:
        return make_response(str(pizza),200)
    else:
        return make_response({"error": f"Pizza with pizza id {pizza_id} does not exist."})
    
@app.route("/toppings/<toppings_id>")
def get_Toppings(toppings_id: int):
    toppings = Toppings.find_toppings(toppings_id = toppings_id)
    if toppings:
        return make_response(str(toppings),200)
    else:
        return make_response({"error": f"Toppings with toppings id {toppings_id} does not exist"})
    
@app.route("/drinks/<name>")
def get_Drinks(name: str):
    drinks1 = drinks.find_drinks(name = name)
    if drinks1:
        return make_response(str(name),200)
    else:
        return make_response({"error": f"Drink with the name {name} does not exist"})
    
@app.route("/desserts/<name>")
def get_Desserts(name: str):
    desserts1 = desserts.find_desserts(name = name)
    if desserts1:
        return make_response(str(name),200)
    else:
        return make_response({"error": f"Dessert with the name {name} does not exist"})
        
@app.route("/customer/<customer_id>")
def get_customer(customer_id: int):
    customer = Customer.FindCustomer(customer_id=customer_id)
    if customer:
        return make_response(print(customer), 200)
    else:
        return make_response({"error": f"Customer with customer id {customer_id} does not exist."})
    
@app.route("/order/<order_id>")
def get_order(order_id: int):
    order = Order.FindOrder(order_id=order_id)
    if order:
        return make_response(print(order), 200)
    else:
        return make_response({"error": f"Order with order id {order_id} does not exist."})
    
@app.route("/cancel/<order_id>")    
def cancel_order(order_id: int):
    order = Order.FindOrder(order_id=order_id)
    if order:
        cancelled_order = Order.CancelOrder(order)
        return make_response(print(cancelled_order), 200)
    else:
        return make_response({"error": f"Order with order id {order_id} does not exist."})
    
@app.route("/create", methods=["GET"])
def create_customer_template():
    return render_template("create_customer.html")

@app.route("/create", methods=["POST"])
def create_customer():
    name = request.form["name"]
    phone_number = request.form["phone_number"]
    address = request.form["address"]
    district_code = request.form["district_code"]
    city = request.form["city"]
    
    customer = Customer.FindCustomer(phone_number=phone_number)
    if customer is not None:
        return make_response({"error": f"Customer with phone number {phone_number} already exists."}, 400)
    
    customer = Customer.FindCustomer(address=address)
    if customer is not None:
        return make_response({"error": f"Customer with address {address} already extists."}, 400)
    
    try:
        customer = Customer.CreateCustomer(name=name, phone=phone_number, address=address, district=district_code, city=city)
    except Exception as ex:
        return make_response({"error": f"Could not create customer {str(ex)}."}, 400)
    
    return make_response({"success": str(customer)}, 200)

@app.route("/order", methods=["GET"])
def create_order_template():
    pizzas = Pizza.get_pizzas()
    drinks1 = drinks.get_drinks()
    desserts1 = desserts.get_desserts()
    
    return render_template("create_order.html", pizzas=pizzas, drinks=drinks1, desserts=desserts1)

@app.route("/order", methods=["POST"])
def create_order():
    customer_id = request.form["customer_id"]
    discount = request.form["discount_code"]
    items = {}
    
    pizzas = Pizza.get_pizzas()
    for item in pizzas:
        items[item.name] = request.form[item.pizza_id]
    
    if len(items) == 0:
        return make_response({"error": "Cannot place an order without at least one pizza."}, 400)
        
    drinks1 = drinks.get_drinks()
    for item in drinks1:
        items[item.name] = request.form[item.drink_id]
    
    desserts1 = desserts.get_desserts()
    for item in desserts1:
        items[item.name] = request.form[item.dessert_id]
        
    customer =  Customer.FindCustomer(customer_id=customer_id)   
    if customer is None:
        name = request.form["name"]
        phone_number = request.form["phone_number"]
        address = request.form["address"]
        district_code = request.form["district_code"]
        city = request.form["city"]
          
        if Customer.FindCustomer(phone_number=phone_number) is not None:
            customer = Customer.FindCustomer(phone_number=phone_number)
      
        elif Customer.FindCustomer(address=address) is not None:
            customer = Customer.FindCustomer(address=address)
            
        else:
            try:
                customer = Customer.CreateCustomer(name=name, phone=phone_number, address=address, district=district_code, city=city)
            except Exception as ex:
                return make_response({"error": f"Could not create customer {str(ex)}."}, 400)
    
    if Order.FindOrder(discount_code=discount):
        return make_response({"error": f"Discount code {discount} is not valid."}, 400)
    
    try:
        order = Order.CreateOrder(customer=customer.id, discount=discount, items=items)
    except Exception as ex:
        return make_response({"error": f"Could not create order {str(ex)}"}, 400)
    
    return make_response({"success": str(order)})
    
    

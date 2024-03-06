
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {"id": 1, "name": "Espresso", "price": 3.50},
    {"id": 2, "name": "Americano", "price": 4.00},
    {"id": 3, "name": "Cappuccino", "price": 4.50},
    {"id": 4, "name": "Latte", "price": 5.00},
    {"id": 5, "name": "Mocha", "price": 5.50},
]

cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products, cart=cart)

@app.route('/menu')
def menu():
    return render_template('menu.html', products=products)

@app.route('/cart')
def my_cart():
    return render_template('cart.html', cart=cart)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html', cart=cart)

@app.route('/api/products')
def get_products():
    return jsonify(products)

@app.route('/api/cart', methods=['POST'])
def update_cart():
    data = request.get_json()
    product_id = data['id']
    quantity = data['quantity']

    for product in products:
        if product['id'] == product_id:
            product['quantity'] = quantity

    return jsonify(cart)

@app.route('/api/checkout', methods=['POST'])
def process_checkout():
    data = request.get_json()
    name = data['name']
    email = data['email']
    address = data['address']

    # Process payment and create order

    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)

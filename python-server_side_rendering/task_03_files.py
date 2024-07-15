from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/items")
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except FileNotFoundError:
        items_list = []

    return render_template('items.html', items=items_list)

def read_json():
    with open('products.json') as f:
        return json.load(f)

def read_csv():
    with open('products.csv', newline='') as f:
        return list(csv.DictReader(f))

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    else:
        return render_template('product_display.html', error='Wrong source')

    if id is not None:
        products = [product for product in products if product['id'] == id]
        if not products:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

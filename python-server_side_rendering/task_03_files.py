from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_data():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except Exception:
        return []

def load_csv_data():
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            return [
                {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                for row in reader
            ]
    except Exception:
        return []

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []

    # Choix de la source
    if source == 'json':
        products = load_json_data()
    elif source == 'csv':
        products = load_csv_data()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # Filtrage par ID
    if product_id is not None:
        filtered = [product for product in products if product['id'] == product_id]
        if not filtered:
            error = "Product not found"
        products = filtered

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)

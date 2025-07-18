from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def load_sql_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [
            {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            for row in rows
        ]
    except Exception:
        return []

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None
    products = []

    if source == 'json':
        products = load_json_data()
    elif source == 'csv':
        products = load_csv_data()
    elif source == 'sql':
        products = load_sql_data()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id is not None:
        filtered = [product for product in products if product['id'] == product_id]
        if not filtered:
            error = "Product not found"
        products = filtered

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)

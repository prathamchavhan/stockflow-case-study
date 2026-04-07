from flask import Flask, request, jsonify

app = Flask(__name__)

products = []
inventory = []

@app.route('/api/products', methods=['POST'])
def create_product():
    try:
        data = request.json

        # validation
        required = ['name', 'sku', 'price', 'warehouse_id']
        if not all(field in data for field in required):
            return {"error": "Missing required fields"}, 400

        # check duplicate SKU
        for p in products:
            if p['sku'] == data['sku']:
                return {"error": "SKU already exists"}, 400

        product_id = len(products) + 1

        product = {
            "id": product_id,
            "name": data['name'],
            "sku": data['sku'],
            "price": float(data['price']),
            "threshold": data.get('threshold', 10)
        }

        products.append(product)

        inv = {
            "product_id": product_id,
            "warehouse_id": data['warehouse_id'],
            "quantity": data.get('initial_quantity', 0)
        }

        inventory.append(inv)

        return {"message": "Product created", "product_id": product_id}, 201

    except Exception as e:
        return {"error": str(e)}, 500


@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    try:
        alerts = []

        for inv in inventory:
            product = next((p for p in products if p['id'] == inv['product_id']), None)

            if product and inv['quantity'] < product['threshold']:
                alerts.append({
                    "product_id": product['id'],
                    "product_name": product['name'],
                    "sku": product['sku'],
                    "warehouse_id": inv['warehouse_id'],
                    "warehouse_name": "Main Warehouse",
                    "current_stock": inv['quantity'],
                    "threshold": product['threshold'],
                    "days_until_stockout": 7,
                    "supplier": {
                        "id": 1,
                        "name": "Demo Supplier",
                        "contact_email": "supplier@test.com"
                    }
                })

        return {
            "alerts": alerts,
            "total_alerts": len(alerts)
        }

    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == '__main__':
    app.run(debug=True)
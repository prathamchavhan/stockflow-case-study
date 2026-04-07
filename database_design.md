## Database Design

Company(id, name)

Warehouse(id, company_id, name)

Product(id, name, sku UNIQUE, price, threshold)

Inventory(id, product_id, warehouse_id, quantity)

Supplier(id, name, email)

Product_Supplier(product_id, supplier_id)

Inventory_Log(id, product_id, warehouse_id, change, timestamp)
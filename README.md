
# StockFlow Case Study  
Name: Pratham Chavhan  
Role: Backend Engineering Intern  

---

## Part 1: Code Review & Debugging

### Issues I Found
- Missing input validation  
- SKU uniqueness not checked  
- Multiple commits causing inconsistency  
- No error handling  
- Price not validated  
- Optional fields not handled  

### Fix
Improved code ensures validation, single transaction, and error handling.

---

## Part 2: Database Design

### Tables
- Company  
- Warehouse  
- Product  
- Inventory  
- Inventory_Log  
- Supplier  
- Product_Supplier  

### Notes
- SKU is unique  
- Inventory supports multiple warehouses  
- Logs track stock changes  

---

## Part 3: Low Stock API

### Approach
- Used JOIN query for performance  
- Supports multiple warehouses  
- Includes supplier info  

---

## Assumptions
- Threshold per product  
- Simplified sales logic  
- One supplier per product  

---

## Conclusion
The solution focuses on data consistency, scalability, and efficient API design.

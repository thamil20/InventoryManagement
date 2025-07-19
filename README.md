# 🛍️ Resale Inventory Management App

This is a custom-built desktop application designed to help track and manage inventory for a small resale business. 
It is being developed for my girlfriend and her mother as they embark on a new business venture. 
The application provides a clean, user-friendly interface for entering, updating, and analyzing product data, helping 
them stay organized and focused on growing their business.

---

## ✅ Project Goals

- Simplify product tracking and inventory management.
- Maintain accurate records of all purchases and sales.
- Track income and expenses over time.
- Provide useful financial insights and reports to support business decisions.

---

## 📄 Application Pages

---

### 🏠 Home Page (Main Menu)

#### 🎉 COMPLETED
- [x] Add buttons to navigate to each page (Need pages to add functionality) 
- [x] Simple, clean layout with spacing and styling

---

### ➕ Add Inventory Page

#### ✅ TODO
- [ ] Input fields:
  - [ ] Product Name  
  - [ ] Product Type  
  - [ ] Product Age  
  - [ ] Product Image (Upload/File Picker)  
  - [ ] Purchase Price  
- [ ] "Add" button:
  - [ ] Validate required fields  
  - [ ] Store data in `CurrentInventory` table  
  - [ ] Save image path to database  
  - [ ] Clear input fields after submission  

#### 🎉 COMPLETED
- _No tasks completed yet_

---

### 📦 Current Inventory Page

#### ✅ TODO
- [ ] Display inventory in a scrollable table or card layout  
- [ ] For each item:
  - [ ] Show Name, Type, Age, Image Preview, and Price  
  - [ ] Edit button to update any field  
  - [ ] Delete button to remove item from database  
  - [ ] "Mark as Sold" button:
    - [ ] Prompt for:
      - [ ] Place of Sale  
      - [ ] Sale Price  
    - [ ] Move item to `SoldInventory` table  
    - [ ] Remove item from `CurrentInventory` table  

#### 🎉 COMPLETED
- _No tasks completed yet_

---

### ✅ Sold Inventory Page

#### ✅ TODO
- [ ] Display table of sold items with:
  - [ ] Name, Type, Age, Purchase Price, Sale Price, Date Sold, Place of Sale  
- [ ] Filter or sort by date, sale platform, or item type  

#### 🎉 COMPLETED
- _No tasks completed yet_

---

### 📈 Income Page

#### ✅ TODO
- [ ] Toggle View:
  - [ ] Monthly Income  
  - [ ] Year-to-Date Income  
- [ ] Graph:
  - [ ] Show Gross Revenue over time  
  - [ ] Show Expenses over time  
  - [ ] Show Net Profit  
- [ ] Data Table:
  - [ ] Gross Revenue = SUM(sale_price)  
  - [ ] Expenses = SUM(expense amounts)  
  - [ ] Estimated Taxes (e.g. 15%)  
  - [ ] Net Income = Revenue - Expenses - Taxes  
- [ ] Export to CSV (optional)  

#### 🎉 COMPLETED
- _No tasks completed yet_

---

## 🛠️ Backend System

---

### 📦 Database Schema

#### ✅ TODO
- [ ] Create `CurrentInventory` table with:
  - [ ] id, name, type, age, image_path, price  
- [ ] Create `SoldInventory` table with:
  - [ ] id, name, type, age, image_path, purchase_price, sale_price, date_sold, place_of_sale, notes  
- [ ] Create `Expenses` table (optional) with:
  - [ ] id, description, amount, date  

#### 🎉 COMPLETED
- _No tables created yet_

---

### 🔁 Database Functionality

#### ✅ TODO
- [ ] Add Inventory Item → Insert into `CurrentInventory`  
- [ ] Edit Inventory Item → Update record in `CurrentInventory`  
- [ ] Delete Inventory Item → Remove from `CurrentInventory`  
- [ ] Mark Item as Sold:
  - [ ] Prompt for sale info  
  - [ ] Move item to `SoldInventory`  
  - [ ] Remove from `CurrentInventory`  
- [ ] Fetch Current Inventory → Query all from `CurrentInventory`  
- [ ] Fetch Sold Inventory → Query all from `SoldInventory`  
- [ ] Add Expense Record (optional) → Insert into `Expenses`  
- [ ] Calculate Income Summary:
  - [ ] Gross Revenue  
  - [ ] Expenses  
  - [ ] Estimated Taxes  
  - [ ] Net Income  

#### 🎉 COMPLETED
- _No functions completed yet_

---

## 💾 Backend Engine Overview

The backend uses **SQLite**, a file-based relational database, integrated directly with Python using `sqlite3`. 
All database logic is centralized in a module like `db_manager.py`.

- Keeps logic separate from the GUI for clarity and maintenance.
- Ensures data consistency and avoids duplication across pages.
- All tables are created on first launch if they don't exist.
- Query functions handle all `INSERT`, `UPDATE`, `DELETE`, and `SELECT` operations.
- Transactions (like "mark as sold") are handled atomically to prevent data loss.

---

## 📎 Project Status

✅ Planning & Design  
✅ README with TODO Tracking  
✅ Main Menu Complete  
🚧 GUI Pages (in progress)  
🚧 Backend Database & Logic (in progress)

---

## 🤝 Acknowledgements

This app is a labor of love created to support my girlfriend and her mother in launching their resale business. 
Its goal is to empower small-scale entrepreneurs with the tools they need to succeed.

---

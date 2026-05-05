# Pizza-Ordering-System-Python
A Python console-based pizza ordering system that allows users to order multiple pizzas with size selection (S/M/L), pepperoni topping, extra cheese, and calculates the total bill. Perfect for practicing loops, conditionals, and user input validation.

# 🍕 Pizza Ordering System (Python Console App)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-Completed-brightgreen)

## 📌 Overview
This is a **simple yet complete pizza ordering system** that runs in the terminal. Customers can order multiple pizzas, choose sizes, add pepperoni and extra cheese, and receive a final bill with itemized pricing.

> Great for learning: loops, conditional statements, user input validation, and accumulators.

## ✨ Features
- Displays price menu at the start.
- Supports **Small (₹100)**, **Medium (₹200)**, **Large (₹300)**
- Pepperoni topping:
  - ₹30 for Small.
  - ₹50 for Medium/Large.
- Extra cheese: **₹20** (any size).
- Allows **multiple pizzas in one order**
- Validates user inputs (S/M/L, Y/N).
- Shows price per pizza and final total with pizza count.

## 🛠️ How It Works (Logic Overview)
1. **Menu displayed** once at the beginning.
2. **Loop** runs for each pizza:
   - User picks size → base price set.
   - Asks for pepperoni → adds cost.
   - Asks for extra cheese → adds cost.
   - Displays individual pizza price.
   - Adds to total bill.
3. Asks if user wants another pizza.
4. After loop ends, shows **final bill** (total pizzas + grand total).

## 🚀 How to Run
### Prerequisites
- Python 3.x installed

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/SachinKumar-IT/Pizza-Ordering-System.git

## 🖥️ Demo Output

```DEMO OUTPUT
===== PIZZA PRICE MENU =====
Small Pizza  : 100 Rs
Medium Pizza : 200 Rs
Large Pizza  : 300 Rs
Pepperoni    : 30 Rs (Small) / 50 Rs (Medium/Large)
Extra Cheese : 20 Rs
=============================

--- Pizza #1 ---
What size pizza you want (S/M/L)? M
Medium Pizza Price is 200 Rs
Do you want Pepperoni (Y/N)? Y
Added Pepperoni for 50 Rs
Do you want extra cheese (Y/N)? Y
Added extra cheese for 20 Rs
Price for this pizza: 270 Rs

Do you want to order another pizza? (Y/N): N

===== FINAL BILL =====
Total pizzas ordered: 1
Your total bill is: 270 Rs
=====================

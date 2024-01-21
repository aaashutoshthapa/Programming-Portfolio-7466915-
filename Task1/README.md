********BPP Pizza Price Calculator********

**Overview**

The "BPP Pizza Price Calculator" is a Python program designed to calculate the total price of a pizza order, considering various factors such as the number of pizzas ordered, delivery preferences, discounts for specific days, and discounts for app usage.

**Usage**
1. To use the calculator, run the Python script, and it will prompt you for the following information:
2. Number of Pizzas Ordered: Enter a non-negative integer representing the quantity of pizzas.
3. Delivery Preference: Enter 'yes' or 'no', or 'y' or 'n' to indicate whether delivery is required.
4. Confirmation if it's Tuesday: Enter 'yes' or 'no', or 'y' or 'n' to confirm if it's Tuesday.

Confirmation of App Usage: Enter 'yes' or 'no', or 'y' or 'n' to confirm if the customer used the app.

The program will then calculate the total price based on the provided information and display a detailed receipt breakdown.

**Functions**
inp()
This function retrieves user inputs related to pizza orders and services. It ensures valid inputs for the number of pizzas, delivery preference, confirmation if it's Tuesday, and confirmation of app usage.

delivery_cost(delivery, no_of_pizza)
Calculates the delivery cost based on the delivery preference and the number of pizzas ordered.

day_discount(day, total_price)
Calculates the discount amount based on a specified day.

app_discount(app, total_price)
Calculates the discount amount based on whether the customer used an app for the order.

calculate_total_price(no_of_pizza, delivery, day, app)
Calculates the total price of a pizza order considering the cost of pizzas, delivery cost, day-based discount, and app-based discount.

display(total_price)
Displays a detailed breakdown and grand total of the pizza order, including the total pizza price, Tuesday discount, App discount, delivery cost, and the grand total.

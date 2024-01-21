# __BPP Pizza Price Calculator__



## __Overview__

The "BPP Pizza Price Calculator" is a Python program designed to calculate the total price of a pizza order, considering various factors such as the number of pizzas ordered, delivery preferences, discounts for specific days, and discounts for app usage.


## __Usage__
1. To use the calculator, run the Python script, and it will prompt you for the following information:
2. Number of Pizzas Ordered: Enter a non-negative integer representing the quantity of pizzas.
3. Delivery Preference: Enter 'yes' or 'no', or 'y' or 'n' to indicate whether delivery is required.
4. Confirmation if it's Tuesday: Enter 'yes' or 'no', or 'y' or 'n' to confirm if it's Tuesday.
Confirmation of App Usage: Enter 'yes' or 'no', or 'y' or 'n' to confirm if the customer used the app.
The program will then calculate the total price based on the provided information and display a detailed receipt breakdown.

## __Notes__
1. Pizza cost: $12 per pizza.
2. Delivery cost: $2.5 if delivery is requested and the number of pizzas is less than 5, otherwise $0.
3. Tuesday discount: 50% off if it's Tuesday, otherwise $0.
4. App discount: 25% off if the customer used the app, otherwise $0.

## __Outputs of Program are Below __

### 1.  simple order for collection, not on a Tuesday, made over the phone.
```
BPP Pizza Price Calculator
=========================

How many pizzas ordered? 4

Is delivery required? n

Is it Tuesday? n

Did the customer use the app? n



           BPP pizza recipt
========================================
Total pizza price:        48.00 
Tuesday discount:         -0.00 
App discount:             -0.00 
Delivery cost             +0.00 
========================================
GRAND TOTAL:             £48.00
```

### 2.the same order, with delivery required. So the delivery charge is added in.
```
BPP Pizza Price Calculator
=========================

How many pizzas ordered? 4

Is delivery required? y

Is it Tuesday? n

Did the customer use the app? n



           BPP pizza recipt
========================================
Total pizza price:        48.00
Tuesday discount:         -0.00
App discount:             -0.00
Delivery cost             +2.50
========================================
GRAND TOTAL:             £50.50
```

### 3.  placed the same order, but used the app to score a 25% discount. Note there is some rounding here
```
BPP Pizza Price Calculator
=========================

How many pizzas ordered? 4

Is delivery required? y

Is it Tuesday? n

Did the customer use the app? y



           BPP pizza recipt
========================================
Total pizza price:        48.00
Tuesday discount:         -0.00
App discount:             -9.47
Delivery cost             +2.50
========================================
GRAND TOTAL:             £37.88
```

### 4. collecting pizzas on a Tuesday, having used the app
```
BPP Pizza Price Calculator
=========================

How many pizzas ordered? 4

Is delivery required? n

Is it Tuesday? y

Did the customer use the app? y



           BPP pizza recipt
========================================
Total pizza price:        48.00
Tuesday discount:         -9.00
App discount:             -4.50
Delivery cost             +0.00
========================================
GRAND TOTAL:             £18.00
```

### 5.  handlling erroneous inpu
```
BPP Pizza Price Calculator
=========================

How many pizzas ordered? -1
Invalid input. Please enter a valid number

How many pizzas ordered? cheese
Invalid input. Please enter a valid number

How many pizzas ordered? banana
Invalid input. Please enter a valid number

How many pizzas ordered? 4

Is delivery required? dunno
Please enter 'yes', 'no', 'y', 'n',Can be both in capslock or not.

Is delivery required? Y

Is it Tuesday? wednesday
Please enter 'yes', 'no', 'y', 'n',Can be both in capslock or not.

Is it Tuesday? N

Did the customer use the app? Y



           BPP pizza recipt
========================================
Total pizza price:        48.00
Tuesday discount:         -0.00
App discount:             -9.47
Delivery cost             +2.50
========================================
GRAND TOTAL:             £37.88
```

# SO THIS COMPLETES TASK 1 WHICH IS PIZZA CALCULATOR 






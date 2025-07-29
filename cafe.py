menu = {
    "Paneer Butter Masala": 180,
    "Veg Biryani": 150,
    "Masala Dosa": 70,
    "Chicken Curry": 200,
    "Mutton Biryani": 250,
    "Pav Bhaji": 90,
    "Chole Bhature": 100,
    "Fried Rice": 120,
    "Dal Tadka": 130,
    "Rajma Chawal": 110,
    "Samosa": 20,
    "Vada Pav": 25,
    "Idli Sambar": 50,
    "Aloo Paratha": 60,
    "Gulab Jamun": 40
}
print("Welcome")
for item, price in menu.items():
    print(f"{item}: ₹{price}")

order_total = 0
item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
    order_total += menu[item]
    print ("Your item {item_1 has been added}")
else:
    print("Ordered item is not available yet")
another_order = input ("Do you want to add another item? (Yes/No)")
if another_order=="Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print (f"Ordered item  {item_2} is not available yet")
print(f"The total amount to pay is: {order_total}")

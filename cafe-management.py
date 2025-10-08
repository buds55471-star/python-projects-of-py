menu = {
    'Pizza':40,
    'Burger':50,
    'Salad':60,
    'Coffee':70
}


print("Welcome to Python Restraunt")
print("Pizza:40\nBurger:50\nSalad:60\nCoffee:70")

order_total = 0
item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total +=menu[item_1]#0+40 =  40
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not Available yet!")

another_order = input("Do you want to add another item?(Yes/No)")
if  another_order == "Yes":
    item_2 = input("Enter the second item =")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The amount of items to pay is {order_total}")


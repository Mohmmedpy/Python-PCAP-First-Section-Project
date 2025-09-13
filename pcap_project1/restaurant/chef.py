def add_dish(menu, name, price):
    if name in menu:
        print(f"Dish'{name}' already exists")
    else:
        menu[name] = {"name": name, "price": price, "available": True}

def remove_dish(menu,name):
    if name in menu:
        del menu[name]
    else:
        print(f"Dish'{name}'not found")

def update_price(menu, name, new_price):
    if name in menu:
        menu[name]["price"] = new_price
    else:
        print(f"Dish'{name}'not found")

def place_order(menu, name):
    if name in menu:
        if menu[name]["available"]:
            menu[name]["available"] = False
        else:
            print(f"Dish '{name}' is already ordered")
    else:
        print(f"Dish '{name}'not found")

def display_menu(menu):
    for dish in menu.values():
        status = "Available" if dish["available"] else "Ordered"
        print(f"{dish['name']} - ${dish['price']:.2f} - {status}")


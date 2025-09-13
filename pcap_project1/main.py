from restaurant import chef

def main():
    menu = {}

    chef.add_dish(menu, "Pizza", 12.99)
    chef.add_dish(menu, "Pasta", 9.99)
    chef.add_dish(menu, "Salad", 6.99)

    print("--- Menu ---")
    chef.display_menu(menu)

    chef.place_order(menu, "Pizza")
    print("--- After Ordering Pizza ---")
    chef.display_menu(menu)

    chef.update_price(menu, "Pizza", 13.99)
    menu["Pizza"]["available"] = True  
    print("--- After Updating Pizza Price ---")
    chef.display_menu(menu)

if __name__ == "__main__":
    main()
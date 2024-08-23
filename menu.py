# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            customer_order = input('What would you like to order? (Numbers only)')

            # 3. Check if the customer typed a number
            if customer_order.isdigit() :
                # Convert the menu selection to an integer
                customer_order_number = int(customer_order)

                # 4. Check if the menu selection is in the menu items
                if customer_order_number in menu_items :
                    # Store the item name as a variable
                    customer_order_details = menu_items[customer_order_number]
                    # Ask the customer for the quantity of the menu item
                    quantity_quesiton = input("And how many would you like huh?")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity_quesiton.isdigit() :
                        quantity_quesiton = int(quantity_quesiton)
                    else :
                        print('Invalid selction... defaulting to 1 item')
                        quantity_quesiton = 1
                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": customer_order_details['Item name'],
                        "Price": customer_order_details['Price'],
                        "Quantity": quantity_quesiton
                    })
                    # Tell the customer that their input isn't valid
            else :
                print('Im sorry... IM SORRY! Your order isn\'t valid :\()')

                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").upper()
        # 5. Check the customer's input
        match keep_ordering :
                # Keep ordering
                case 'Y' :
                # Exit the keep ordering question loop
                    print('Thanks for the order!')
                    break
                # Complete the order
                case 'N' :
                # Since the customer decided to stop ordering, thank them for
                # their order
                    print('Thank you so much for ordering, that means sooo much')
                # Exit the keep ordering question loop
                    place_order = False
                    break
                # Tell the customer to try again
                case _ :
                    print('Errrrm, that didn\'t exactly work. \
                    Please reply with "Y" to continue ordering \
                    or with "N" to stop')
                    continue

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
print(order_list)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for x in order_list :
# 7. Store the dictionary items as variables
    item_name = x["Item name"]
    item_price = x["Price"]
    quantity = x["Quantity"]  # Fixed variable name from quantity_quesiton to quantity
    
    # 8. Calculate the number of spaces for formatted printing
    name_spaces = 26 - len(item_name)
    price_spaces = 8 - len(f"${item_price:.2f}")
    
    # 9. Create space strings
    name_space_str = ' ' * name_spaces
    price_space_str = ' ' * price_spaces    

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{name_space_str}| ${item_price:.2f}{price_space_str}| {quantity}")

# 11. Calculate the cost of the order using list comprehension
total_cost = sum(item["Price"] * item["Quantity"] for item in order_list)

# Print the total cost
print(f"\nTotal Cost: ${total_cost:.2f}")
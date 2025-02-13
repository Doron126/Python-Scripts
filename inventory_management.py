from functools import reduce
from operator import mul
import re
from tabulate import tabulate

def inventory_mgmt():
    manu = """Choose an option:
1. Add Product
2. View Products
3. Update Product
4. Delete Product
5. Calculate Inventory Value
6. Find Most Expensive Product
7. Exit"""

    inventory = []

    def add_product():
        product_directory = {}
        product_name = input("\nEnter product name: ").strip().capitalize()
        if not re.match(r"^[a-zA-Z ']+$", product_name):
            print("\nYou must put an alphabetic name.\n")
            return
        for product in inventory:
            if product["Name"] == product_name:
                print("\nName allready exists.\n")
                return
        quantity = input("Enter quantity: ").strip()
        if not quantity.isdecimal():
            print("\nInvalid, put numbers only.\n")
            return
        price_per_unit = input("Enter price per unit: ").strip()
        if not price_per_unit.isdecimal():
            print("\nInvalid, put numbers only.\n")
            return
        product_directory["Name"] = f"{product_name}"
        product_directory["Quantity"] = f"{quantity}"
        product_directory["Price Per Unit"] = f"{price_per_unit}"
        inventory.append(product_directory)

    def view_products():
        if not inventory:
            print("\nThe inventory is empty\n")
            return
        else:
            headers = ["#", "Name", "Quantity", "Price Per Unit"]
            table_data = [[index, product["Name"], product["Quantity"], product["Price Per Unit"]] for index, product in enumerate(inventory, start=1)]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

    def update_product():
        if not inventory:
            print("\nThe inventory is empty\n")
            return
        else:
            found = False
            product_choice = input("Enter the name of the product you want to update: ").capitalize().strip()
            for product in inventory:
                if product["Name"] == product_choice:
                    found = True
                    category_choice = input("Which category do you want to update? (Name\\Quantity\\Price per Unit): ").capitalize().strip()
                    if category_choice == "Name" or category_choice == "Quantity" or category_choice == "Price per unit":
                        new_data = input("What is the new value you want to put?: ").capitalize()
                        if category_choice == "Name" and not new_data.isalpha():
                            print("\nYou must put an alphabetic name.\n")
                            return
                        elif category_choice == "Price per unit" or category_choice == "Quantity" and not new_data.isdecimal():
                            print("\nInvalid, put numbers only.\n")
                            return
                        product[category_choice] = new_data
                    else:
                        print("\nPlease put a valid category name. (Name\\Quantity\\Price per Unit)\n")
                if found == False:
                    print("\nNot found.\n")

    def delete_product():
        if not inventory:
            print("\nThe inventory is empty\n")
            return
        product_choice = input("Enter the name of the product you want to delete: ").capitalize().strip()
        result = False
        for product in inventory:
            if product["Name"] == product_choice:
                result = True
                print(f"\n{product_choice} have been deleted.\n")
                inventory.remove(product)
            if result == False:
                print("\nName not found.\n")

    def calculate_inventory_value():
        if not inventory:
            print("\nThe inventory is empty\n")
            return
        items = []
        for item in inventory:
            calc = []
            for value in item.values():
                if value.isdigit():
                    calc.append(int(value))
            res = reduce(mul, calc)
            items.append(res)
        print(f"\nTotal inventory value: ${(sum(items))}.\n")

    def most_expensive_product():
        if not inventory:
            print("\nThe inventory is empty\n")
            return
        elif len(inventory) == 1:
            print("\nYou have only 1 item in the inventory.\n")
            return
        else:
            max_price = max(int(product["Price Per Unit"]) for product in inventory)
            most_expensive = [product for product in inventory if int(product["Price Per Unit"]) == max_price]
            for product in most_expensive:
                print(f"""The most expensive product(s) are:
- {product["Name"]} with the value of {product["Price Per Unit"]}.""")
            print()

    while True:
        print(manu)
        user_choice = input("\nWhich action do you want to choose?\n")

        if user_choice == "1":
            add_product()

        elif user_choice == "2":
            view_products()

        elif user_choice == "3":
            update_product()

        elif user_choice == "4":
            delete_product()

        elif user_choice == "5":
            calculate_inventory_value()

        elif user_choice == "6":
            most_expensive_product()

        elif user_choice == "7":
            print("Bye!")
            break

        else:
            print("Choose a valid choice!")

inventory_mgmt()
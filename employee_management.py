
import re
def program():
    menu = """Choose a number from the manu:
1. Add Employee
2. Display All Employees
3. Update Employee Details
4. Delete An Employee
5. Calculate Average Salary
6. Exit"""
    employees_list = []
    def add_employee():
        name = input("\nWhat is the name of the employee?:\n").strip().lower()
        if not re.match(r"^[A-Za-z' ]+$", name):
            print("\nYou must put alphabetical name.\n")
            return
        for emp in employees_list:
            if name == emp["Name"]:
                print("\nName already exists.\n")
                return
        age = input("\nWhat is the age of the employee?:\n").strip()
        if not age.isdigit():
            print("\nYou can put numbers only for the age.\n")
            return
        position = input("\nWhat is the position of the employee?:\n").strip().lower()
        if not re.match(r"^[A-Za-z' ]+$", position):
            print("\nYou must put alphabetical position name.\n")
            return
        salary = input("\nWhat is the salary of the employee?:\n").strip()
        if not salary.isdigit():
            print("\nYou can put numbers only for the salary.\n")
            return
        employee = {}
        employee['Name'] = name
        employee['Age'] = age
        employee['Position'] = position
        employee['Salary'] = salary
        employees_list.append(employee)

    def display_employees():
        if len(employees_list) == 0:
            print("\nThe list is empty.")
        else:
            for index, value in enumerate(employees_list, start=1):
                print(f"\n{index} {value}\n")

    def update_employee():
        if len(employees_list) == 0:
            print("\nThe list is empty.")
        else:
            search_name = input("Enter the name you want to search:\n").strip().lower()
            found = False
            for emp in employees_list:
                if emp["Name"] == search_name:
                    found = True
                    ask_category = input("\nWhich category do you want to change? (Name\\Age\\Position\\Salary)\n").strip().capitalize()
                    if ask_category in emp:
                        ask_change = input("What is the new value?\n").strip()
                        if ask_category == "Age" or ask_category == "Salary":
                            if not ask_change.isdigit():
                                print("\nYou can put numbers only in that category.\n")
                                continue
                        elif ask_category == "Name" or ask_category == "Position":
                            if not ask_change.isalpha():
                                print("\nYou can put alphabetical values only in that category.\n")
                                continue
                        emp[ask_category] = ask_change
                    elif ask_category not in emp:
                        print("\nYou must choose a valid category.\n")
            if not found:
                print("\nName not found.\n")

    def delete_employee():
        if len(employees_list) == 0:
            print("\nThe list is empty.")
        else:
            search_delete = input("Enter the name of the employee you want to delete:")
            for i in employees_list:
                if search_delete in i.values():
                    print(f"Employee {i} got deleted.")
                    employees_list.remove(i)
                else:
                    print("\nNot found.")

    def calculate_avg_salary():
        try:
            summarize_salary = sum(int(emp["Salary"]) for emp in employees_list)
            summarize_emp = len(employees_list)
            avg = summarize_salary / summarize_emp
            print(avg)
        except ZeroDivisionError:
            print("\nList is empty.")
    while True:
        
        choose = input(f"\n{menu}\n")

        if choose == '1':
            add_employee()

        elif choose == '2':
            display_employees()

        elif choose == '3':
            update_employee()

        elif choose == '4':
            delete_employee()

        elif choose == '5':
            calculate_avg_salary()

        elif choose == '6':
            print("Goodbye!")
            break
        
        else:
            print("Choose a valid number from the manu.")
            
program()
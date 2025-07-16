# Customer class stores details about a single customer
class Customer:
    def __init__(self, name, room_type):
        self.name = name
        self.room_type = room_type.lower()
        self.days = 0
        self.bill = 0

    # Set how many days the customer is staying
    def set_days(self, days):
        self.days = days
        self.calculate_bill()

    # Calculate the bill based on room type and number of days
    def calculate_bill(self):
        if self.room_type == "single":
            rate = 1000
        elif self.room_type == "double":
            rate = 1800
        elif self.room_type == "deluxe":
            rate = 2500
        else:
            rate = 1000  # default to single room rate

        self.bill = rate * self.days

    # Show the final bill
    def show_bill(self):
        print("\n----- BILL -----")
        print(f"Name       : {self.name}")
        print(f"Room Type  : {self.room_type.capitalize()}")
        print(f"Days Stay  : {self.days}")
        print(f"Total Bill : ₹{self.bill}")
        print("----------------\n")


# Hotel class manages all the customers
class Hotel:
    def __init__(self):
        self.customers = []  # list to store all customer objects

    # Add new customer
    def add_customer(self, name, room_type):
        new_customer = Customer(name, room_type)
        self.customers.append(new_customer)
        print(f"\nCustomer '{name}' added successfully!\n")

    # Find customer by name
    def find_customer(self, name):
        for customer in self.customers:
            if customer.name.lower() == name.lower():
                return customer
        return None

    # Show names of all customers
    def show_customers(self):
        if not self.customers:
            print("\nNo customers yet.\n")
        else:
            print("\nCurrent Customers:")
            for customer in self.customers:
                print(f"- {customer.name} ({customer.room_type})")
            print()

    # Remove customer after checkout
    def checkout_customer(self, name):
        customer = self.find_customer(name)
        if customer:
            customer.show_bill()
            self.customers.remove(customer)
            print(f" '{name}' has been checked out.\n")
        else:
            print(" Customer not found.\n")


# MENU SYSTEM (User Interface)


hotel = Hotel()

while True:
    print("===== Hotel Management Menu =====")
    print("1. Add New Customer")
    print("2. Set Stay Duration")
    print("3. Show Customer Bill")
    print("4. Show All Customers")
    print("5. Checkout Customer")
    print("6. Exit")
    print("=================================")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter customer name: ")
        room_type = input("Enter room type (Single/Double/Deluxe): ")
        hotel.add_customer(name, room_type)

    elif choice == "2":
        name = input("Enter customer name to set stay days: ")
        customer = hotel.find_customer(name)
        if customer:
            days = int(input("Enter number of days: "))
            customer.set_days(days)
            print(" Stay duration updated.\n")
        else:
            print(" Customer not found.\n")

    elif choice == "3":
        name = input("Enter customer name to show bill: ")
        customer = hotel.find_customer(name)
        if customer:
            customer.show_bill()
        else:
            print(" Customer not found.\n")

    elif choice == "4":
        hotel.show_customers()

    elif choice == "5":
        name = input("Enter customer name to checkout: ")
        hotel.checkout_customer(name)

    elif choice == "6":
        print("Exiting the system. Thank you!")
        break

    else:
        print(" Invalid input. Try again.\n")

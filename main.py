from abc import ABC, abstractmethod

# Abstract Class (Abstraction)
class AbstractCustomer(ABC):
    @abstractmethod
    def show_bill(self):
        pass


# Base Class (Encapsulation)
class Customer(AbstractCustomer):
    def __init__(self, name, room_type):
        self._name = name  # private
        self._room_type = room_type.lower()
        self._days = 0
        self._bill = 0

    # Getter for name
    def get_name(self):
        return self._name

    # Set number of days and calculate bill
    def set_days(self, days):
        self._days = days
        self.calculate_bill()

    # Calculate bill based on room type
    def calculate_bill(self):
        rates = {"single": 1000, "double": 1500, "deluxe": 2500}
        rate = rates.get(self._room_type, 1000)  # default to single
        self._bill = self._days * rate

    # Show bill (Polymorphic — will be overridden)
    def show_bill(self):
        print("\n----- BILL -----")
        print(f"Customer Name : {self._name}")
        print(f"Room Type     : {self._room_type.capitalize()}")
        print(f"Days Stayed   : {self._days}")
        print(f"Total Bill    : ₹{self._bill}")
        print("----------------\n")


# Child Class (Inheritance + Polymorphism)
class LuxuryCustomer(Customer):
    def __init__(self, name):
        super().__init__(name, "deluxe")  # Always deluxe room

    # Overriding show_bill (Polymorphism)
    def show_bill(self):
        self.calculate_bill()
        gst = self._bill * 0.18
        total = self._bill + gst
        print("\n----- LUXURY BILL -----")
        print(f"Customer Name : {self._name}")
        print(f"Room Type     : {self._room_type.capitalize()}")
        print(f"Base Bill     : ₹{self._bill}")
        print(f"GST (18%)     : ₹{gst:.2f}")
        print(f"Total Bill    : ₹{total:.2f}")
        print("------------------------\n")


# Hotel Class (Manages all customers)
class Hotel:
    def __init__(self):
        self.customers = []

    # Add customer (normal or luxury)
    def add_customer(self, name, room_type):
        if room_type.lower() == "luxury":
            customer = LuxuryCustomer(name)
        else:
            customer = Customer(name, room_type)
        self.customers.append(customer)
        print(f"{name} added successfully!\n")

    # Find customer by name
    def find_customer(self, name):
        for customer in self.customers:
            if customer.get_name().lower() == name.lower():
                return customer
        return None

    # Show all customers
    def show_customers(self):
        if not self.customers:
            print(" No customers yet.\n")
        else:
            print("\n All Customers:")
            for c in self.customers:
                print(f"- {c.get_name()}")
            print()

    # Checkout customer
    def checkout_customer(self, name):
        customer = self.find_customer(name)
        if customer:
            customer.show_bill()
            self.customers.remove(customer)
            print(f" {name} checked out.\n")
        else:
            print("Customer not found.\n")



# Menu-Driven Program (UI)


hotel = Hotel()

while True:
    print("========= HOTEL MENU =========")
    print("1. Add Customer")
    print("2. Set Stay Days")
    print("3. Show Bill")
    print("4. Show All Customers")
    print("5. Checkout")
    print("6. Exit")
    print("==============================")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        room = input("Enter room type (Single/Double/Deluxe/Luxury): ")
        hotel.add_customer(name, room)

    elif choice == "2":
        name = input("Enter customer name: ")
        c = hotel.find_customer(name)
        if c:
            days = int(input("Enter number of days: "))
            c.set_days(days)
            print(" Stay duration updated.\n")
        else:
            print(" Customer not found.\n")

    elif choice == "3":
        name = input("Enter customer name: ")
        c = hotel.find_customer(name)
        if c:
            c.show_bill()
        else:
            print(" Customer not found.\n")

    elif choice == "4":
        hotel.show_customers()

    elif choice == "5":
        name = input("Enter customer name: ")
        hotel.checkout_customer(name)

    elif choice == "6":
        print(" Exiting Hotel System. Thank you!")
        break

    else:
        print(" Invalid choice. Try again.\n")

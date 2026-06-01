########################################################################
# Task 1 University System
########################################################################

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self) -> str:
        return f"Hello, my name is {self.first_name} {self.last_name}."


class Student(Person):
    def introduce(self) -> str:
        return f"Hi! I'm {self.first_name} {self.last_name}, and I am a student here."


class Lecturer(Person):
    def introduce(self) -> str:
        return f"Good day. I am Professor {self.first_name} {self.last_name}, and I will be your lecturer."


# Example
student = Student("John", "Doe")
print(student.introduce())

lecturer = Lecturer("Jane", "Doe")
print(lecturer.introduce())


########################################################################
# Task 2 Social Media Profile
########################################################################

class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = password

    def check_password(self, password: str) -> bool:
        return self.__password == password

    def change_password(self, old_password: str, new_password: str) -> None:
        if self.check_password(old_password):
            self.__password = new_password
            print("Password successfully updated!")
        else:
            print("Error: Incorrect old password. Action denied.")


# Example
user_profile = Profile("tech_guru", "Secret123")

# Checking password
print(user_profile.check_password("WrongPass"))
print(user_profile.check_password("Secret123"))

# Changing password
user_profile.change_password("WrongPass", "NewSecret567")
user_profile.change_password("Secret123", "NewSecret567")

########################################################################
# Task 3 Online Shop Product
########################################################################

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.__price = None
        self.set_price(price)

    def get_price(self) -> float:
        return self.__price

    def set_price(self, price: float) -> None:
        if price < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = price


# Example
try:
    item = Product("Wireless Mouse", 25.99)
    print(f"Product: {item.name}, Price: ${item.get_price()}")

    item.set_price(29.99)
    print(f"Updated Price: ${item.get_price()}")

    item.set_price(-5.00)
except ValueError as e:
    print(f"Exception caught: {e}")
########################################################################
# Task 4 Payment System
########################################################################

class CreditCardPayment:
    def pay(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount:.2f} securely via payment gateway.")


class PayPalPayment:
    def pay(self, amount: float) -> None:
        print(f"Redirecting to PayPal... Successfully paid ${amount:.2f} using your PayPal balance/linked account.")


class CryptoPayment:
    def pay(self, amount: float) -> None:
        print(f"Blockchain transaction initialized. Transferring ${amount:.2f} equivalent in Crypto.")


# Example
def process_checkout(payment_method, total_amount):
    payment_method.pay(total_amount)

card = CreditCardPayment()
paypal = PayPalPayment()
crypto = CryptoPayment()

process_checkout(card, 150.00)
process_checkout(paypal, 45.50)
process_checkout(crypto, 899.99)

########################################################################
# Task 5  Total Number of Cars
########################################################################

class Car:
    total_cars = 0

    def __init__(self, model: str):
        self.model = model

        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls) -> int:
        return cls.total_cars


# Example
c1 = Car("BMW")
c2 = Car("Mercedes")
c3 = Car("Toyota")

print(Car.get_total_cars())


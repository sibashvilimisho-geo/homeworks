########################################################################
# Task 1 Dog Class
########################################################################

class Dog:
    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age

    def bark(self):

        print(f"{self.name} says: Woof!")

    def info(self):

        print(f"Dog Profile -> Name: {self.name}, Age: {self.age} years old")


# --- Testing Task 1 ---
print("--- Task 1: Dog Class Test ---")
dog1 = Dog("Buddy", 3)
dog1.info()
dog1.bark()

########################################################################
# Task 2 Rectangle Class
########################################################################

class Rectangle:
    def __init__(self, width: float, height: float):

        self.width = width
        self.height = height

    def area(self) -> float:

        return self.width * self.height

    def perimeter(self) -> float:

        return 2 * (self.width + self.height)

    def is_square(self) -> bool:

        return self.width == self.height


# --- Testing Task 2 ---
print("\n--- Task 2: Rectangle Class Test ---")
rect = Rectangle(5, 5)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print(f"Is it a square? {rect.is_square()}")

########################################################################
# Task 3 Bank Account Class
########################################################################

class BankAccount:

    bank_name = "Step Bank"

    def __init__(self, owner: str, initial_balance: float = 0.0):

        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount: float):

        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f} into {self.owner}'s account.")
        else:
            print("Invalid deposit allocation amount requested.")

    def withdraw(self, amount: float):

        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal request must be positive.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f} from {self.owner}'s account.")

    def show_balance(self):

        print(f"Bank: {self.bank_name} | Owner: {self.owner} | Current Balance: ${self.balance:.2f}")


# --- Testing Task 3 ---
print("\n--- Task 3: Bank Account Class Test ---")
account = BankAccount("Alice Smith", 100.0)
account.show_balance()
account.deposit(50)
account.withdraw(200)
account.show_balance()

########################################################################
# Task 4 Students List
########################################################################

class Student:
    def __init__(self, name: str, grade: float):

        self.name = name
        self.grade = grade


class Classroom:
    def __init__(self):

        self.students = []

    def add_student(self, student: Student):

        self.students.append(student)

    def average(self) -> float:

        if not self.students:
            return 0.00
        total_grades = sum(student.grade for student in self.students)
        return round(total_grades / len(self.students), 2)

    def top_student(self) -> str:

        if not self.students:
            return "No students available."

        best_student = max(self.students, key=lambda s: s.grade)
        return best_student.name


# --- Testing Task 4 ---
print("\n--- Task 4: Classroom & Student Track System Test ---")
# 1. Create a Classroom object
my_classroom = Classroom()

# 2. Instantiate individual Student profiles
student1 = Student("John Doe", 8.5)
student2 = Student("Emma Watson", 9.8)
student3 = Student("Robert Downey", 7.2)

# 3. Add student objects into the classroom manager allocation tracking list
my_classroom.add_student(student1)
my_classroom.add_student(student2)
my_classroom.add_student(student3)

# 4. Compute metrics and showcase values
print(f"Classroom Average: {my_classroom.average()}")
print(f"Top Performer:    {my_classroom.top_student()}")
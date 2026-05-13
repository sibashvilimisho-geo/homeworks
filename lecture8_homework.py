print("Task1_min_max")

def find_min_max(*args):
    if args:
        print(f"Min: {min(args)}, Max: {max(args)}")
    else:
        print("No numbers provided")

find_min_max(1,2,3,4,5,6)

print("Task2_calculation")

def calculate(*args, operation="sum"):
    if not args:
        print(0)
        return

    if operation == "sum":
        print(sum(args))
    elif operation == "max":
        print(max(args))
    elif operation == "min":
        print(min(args))
    elif operation == "mult":
        result = 1
        for num in args:
            result *= num
        print(result)
    else:
        print("Invalid operation")

calculate(1,2,3,4,5,6)
calculate(1, 8, 3, 12, operation="max")
calculate(10, -5, 0, operation="min")
calculate(2, 3, 4, operation="mult")

print("Task3_User_Formatting")

user_info = {
    "status": "Active",
    "experience": "5 years",
    "role": "Admin"
}


def format_user(first_name, last_name, **kwargs):
    details = [f"{key}: {value}" for key, value in kwargs.items()]
    details_str = ", ".join(details)
    print(f"{first_name} {last_name} | {details_str}")

format_user("Giorgi", "Kapanadze", **user_info)

print("Task4_Safe_Division")

def safe_divide(a, b):
    if b == 0:
        print("Cannot divide by zero")
    else:
        quotient = a // b
        remainder = a % b
        print(f"({quotient}, {remainder})")

safe_divide(4, 5)
safe_divide(17,0)
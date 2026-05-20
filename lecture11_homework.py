########################################################################
# Task 1 finding negative numbers
########################################################################

from functools import wraps

def check_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                return "only positive numbers are allowed"
        return func(*args, **kwargs)
    return wrapper

@check_positive
def multiply(a, b):
    return a * b

# Testing
print(multiply(5, 4))
print(multiply(-5, 4))


########################################################################
# Task 2 finding called function
########################################################################

def log_results(func):
    @wraps(func)
    def wrapper(num1, num2):
        returned_value = func(num1, num2)

        return f"called function '{func.__name__}', with attributes {num1} and {num2}, returned {returned_value}"
    return wrapper

@log_results
def add(a, b):
    return a + b

@log_results
def subtract(a, b):
    return a - b

# Testing
print(add(10, 15))
print(subtract(50, 20))

########################################################################
# Task 3 time delay
########################################################################

import time


def repeat(times, delay):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)

                if i < times - 1:
                    time.sleep(delay)
        return wrapper
    return decorator

@repeat(times=3, delay=2)
def say_hello():
    print("Hello!")

# Testing
say_hello()

########################################################################
# Task 4 role
########################################################################


current_user = {
    "username": "irakli",
    "role": "admin"
}

def role_required(allowed_role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.get("role") == allowed_role:
                return func(*args, **kwargs)
            else:
                print("Permission denied!")
                return None

        return wrapper
    return decorator

@role_required("admin")
def delete_user(user_id):
    print(f"User with id {user_id} has been deleted.")

@role_required("editor")
def edit_user(user_id):
    print(f"User with id {user_id} has been updated.")

@role_required("user")
def create_user(first_name):
    print(f"User {first_name} has been created.")

# Testing
print("Administrator")
delete_user(5)
edit_user(5)

print("\n Editor")
current_user["role"] = "editor"
delete_user(5)
edit_user(5)
########################################################################
# Task 1 safe_get
########################################################################

def safe_get(lst, index):
    try:
        return lst[index]
    except IndexError:
        print("Error: There is no item with this index")
    except TypeError:
        print("Error: Index must be an integer")

# testing:
my_list = [10, 20, 30]

print(safe_get(my_list, 1))
safe_get(my_list, 5)
safe_get(my_list, "hello")


########################################################################
# Task 2 safe_get_value
########################################################################

def safe_get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print(f"Error: Key '{key}' doesn't exist")
        return None

# testing:
my_dict = {"name": "Anano", "age": 25}

print(safe_get_value(my_dict, "name"))
print(safe_get_value(my_dict, "city"))


########################################################################
# Task 1 try
########################################################################

try:
    number = float(input("Please enter a number: "))
except ValueError:
    print("Error:please enter a number!")
else:
    result = number ** 2
    print(f"{number} in square is {result}")
finally:
    print("Thank you for your time!")
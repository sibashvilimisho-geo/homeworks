print("Task1_total_sum")

numbers = [10, 25, 4, 18, 32, 45, 12, 89, 3, 56, 21, 10, 3, 15, 32, 18, 21]
total_sum = 0

print(f"Numbers:{numbers}")
for num in numbers:
    total_sum += num

print("Total sum:", total_sum)

print("Task2_min_max")

max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Max element:", max_val)
print("Min element:", min_val)

print("Task3_even_odd")

evens = []
odds = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

print("Even numbers:", evens)
print("Odd numbers:", odds)

print("Task4_duplicate")

unique_list = list(set(numbers))

print("Original list:", numbers)
print("Clean list:", unique_list)

print("Task5_list_tuple")

my_tuple = tuple(numbers)

print("This is list:", numbers)
print("this is tuple:", my_tuple)
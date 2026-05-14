print("Task1_sum_of_digits")

def sum_of_digits(n, total=0):
    n = abs(n)
    total += n % 10

    if n // 10 == 0:
        print(total)
    else:
        sum_of_digits(n // 10, total)

sum_of_digits(int(input('enter number:')))

print("Task2_is_even")

is_even = lambda n: n % 2 == 0

num2=int(input("enter number:"))
print(f'entered number is even: {is_even(num2)}')

print("Task3_sorted_students")

students = [
    ("Luka", 15, 85),
    ("Ana", 14, 92),
    ("Giorgi", 16, 78),
    ("Nino", 15, 95)
]

sorted_students = sorted(students, key=lambda x: (x[1], x[2]))

print(sorted_students)

print("Task4_sorted_words")

words = ["banana", "apple", "kiwi", "watermelon", "cherry"]

sorted_words = sorted(words, key=len, reverse=True)

print(sorted_words)

print("Task5_capitalized_words")

words = ["banana", "apple", "kiwi", "watermelon", "cherry"]

capitalized_words = list(map(lambda x: x.capitalize(), words))

print(capitalized_words)

print("Task6_filtered_numbers")

numbers = [5, 12, 7, 18, 3, 24, 9, 15, 78]

filtered_numbers = list(filter(lambda x: x > 10 and x % 3 == 0, numbers))

print(filtered_numbers)
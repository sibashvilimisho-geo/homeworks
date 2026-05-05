print("Task1 Countdown")

n = int(input("Enter a number where from you want to count down: "))

while n >= 0:
    print(n)
    n -= 1
print("Blast off!")

print("Task2 sum count")

total_sum = 0

while True:
    number = int(input("Enter a number (0 for stop): "))
    if number == 0:
        break
    total_sum += number

print(f"Entered number sum is {total_sum}")

print("Task3 guess the number")

secret_num=56

while True:
    guess = int(input("guess number: "))
    if guess > secret_num:
        print('number is too high')
    elif guess < secret_num:
        print('number is too low')
    else:
        print('you guessed right')
        break

print("Task4 no vowels")

word = input("Write a word: ").strip().lower()
vowels = "aeiou"

for ch in word:
    if ch in vowels:
        continue
    print(ch, end="")
print("\n")
print("Task5 range() practice ")

print('0-9')
for i in range(10):
    print(i, end=", ")

print("\n")

print('5-15')
for i in range(5, 15):
    print(i, end=", ")

print("\n")

print('0-20')
for i in range(0,21,2):
    print(i, end=", ")

print("\n")

print('10-1')
for i in range(10, 0, -1):
    print(i, end=", ")
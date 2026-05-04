print("Task1")


user_age = int(input("Enter your age: "))

if 0 <= user_age <= 12:
    print("you are in child age group ")

elif 12 < user_age <= 19:
    print("you are in  teenage group ")

elif 19 < user_age <= 64:
    print("your are in adult age group ")

else:
    print("you are in senior age group")


print("Task2")

score = float(input("Enter your score: "))
attandance = float(input("Enter your attandance in %: "))


if score >= 60 and attandance >= 75:
    print("you passed the cource")

elif score < 60 or attandance < 75:
    print("you failed the cource")


print("Task3")

stud_status = input(" Do you have student status(yes/no): ").strip().lower()
stud_memb = input("Do you have active student membership (yes/no): ").strip().lower()

if stud_status == "yes" and stud_memb == "yes":
    print("you can use premium discount")

elif stud_status == "yes" or stud_memb == "yes":
    print("you can use standart discount")

elif stud_status == "no" and stud_memb == "no":
    print("you don't have discount")


print("Task4")

username = input("Enter your username: ")

if 3 < len(username) < 20 and username.isalnum():
    print("your username is correct")

else:
    print("your username is incorrect, it contains special characters or symbols count are out of given range")
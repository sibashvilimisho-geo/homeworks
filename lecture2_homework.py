####################################################################################
print("Task1: Types")
###################################################################################
# stiring
name1 = "Giorgi"

#integer
num1=15

#float
num2=20.6

#boolean
number_compears=num1<=num2

print((name1), "is", type(name1))

print((num1), "is", type(num1))

print((num2), "is", type(num2))

print((number_compears), "is", type(number_compears))

#################################################################################
print("task2: age calculation")
#################################################################################

birth_year=int(input("Enter your birth year: "))

year_now=2026

print("Your are", (year_now-birth_year), "years old")

################################################################################
print("task3: number describe")
################################################################################

num3=int(input("Enter any integer number: "))

is_negative=num3<0

is_positive=num3>0

is_zero=num3==0

is_even=num3%2==0

is_odd=num3%2==1

print(num3, "is negative:", (is_negative))
print(num3, "is positive:", (is_positive))
print(num3, "is zero:", (is_zero))
print(num3, "is odd:", (is_odd))
print(num3, "is even:", (is_even))

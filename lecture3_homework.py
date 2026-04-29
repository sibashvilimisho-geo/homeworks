print("Task1")

full_name=input("Enter your full name: ").strip()

name_parts=full_name.split(" ")
first_name=name_parts[0]
last_name=name_parts[1]

print(f"Your initials are:{first_name[0].upper()}.{last_name[0].upper()}")

print("Task2")

word=input("Enter any your word, that you want to reverse : ").lower().strip()
print(f'your reverse word is: {word[::-1]}')

print("Task3")

sentence=input("Enter any sentence: ").lower().strip().title()
print(f'your sentence is: {sentence}')

word1=input("Enter word you want to replace: ").lower().strip().title()
word2=input("Enter word you want to be replaced with: ").lower().strip().title()

print(f'your final sentence is: {sentence.replace(word1,word2)}')
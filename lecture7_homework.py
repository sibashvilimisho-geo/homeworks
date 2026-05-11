print("Task1_repetition")

words = ["apple", "banana", "apple", "cherry", "banana", "apple", "orange"]
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)

print("Task2_merge")

dict1 = {'a': 11, 'b': 20, 'c': 30}
dict2 = {'b': 25, 'c': 45, 'd': 40}
merge_dict = {}

for key in set(dict1.keys()) | set(dict2.keys()):
    if key in dict1 and key in dict2:
        merge_dict[key] = [dict1[key], dict2[key]]
    elif key in dict1:
        merge_dict[key] = dict1[key]
    else:
        merge_dict[key] = dict2[key]

print(merge_dict)

print("Task3_reverse")

original_dict = {'a': 3, 'b': 7, 'c': 5, 'd': 9, 'e':55}
reversed_dict = {value: key for key, value in original_dict.items()}

print(reversed_dict)

print("Task4_films")

films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}
films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}

print("Films that are in both:", films1 & films2)
print("Films that are loved by first person:", films1 - films2)
print("Films that are loved by second:", films2 - films1)
print("All unic films:", films1 | films2)

print("Task5_Students")

students = {
    "კლასი 10A": {
        "გიორგი": {
            "ასაკი": 16,
            "საშუალო_ქულა": 8.7,
            "საგნები": {"მათემატიკა": {"ქულა": 9}, "ფიზიკა": {"ქულა": 8}, "ისტორია": {"ქულა": 9},
                        "ინგლისური": {"ქულა": 10}},
            "დასწრება": 92,
            "დამატებითი": ["ფეხბურთი", "პროგრამირება"]
        },
        "ანა": {
            "ასაკი": 15,
            "საშუალო_ქულა": 9.4,
            "საგნები": {"მათემატიკა": {"ქულა": 10}, "ფიზიკა": {"ქულა": 9}, "ისტორია": {"ქულა": 8},
                        "ინგლისური": {"ქულა": 10}},
            "დასწრება": 98,
            "დამატებითი": ["ცეკვა"]
        },
        "დავით": {
            "ასაკი": 16,
            "საშუალო_ქულა": 7.2,
            "საგნები": {"მათემატიკა": {"ქულა": 6}, "ფიზიკა": {"ქულა": 7}, "ისტორია": {"ქულა": 8},
                        "ინგლისური": {"ქულა": 9}},
            "დასწრება": 75,
            "დამატებითი": ["კალათბურთი", "პროგრამირება"]
        }
    },
    "კლასი 10B": {
        "მარიამ": {
            "ასაკი": 15,
            "საშუალო_ქულა": 9.1,
            "საგნები": {"მათემატიკა": {"ქულა": 9}, "ბიოლოგია": {"ქულა": 10}},
            "დასწრება": 95,
            "დამატებითი": ["მუსიკა", "ხატვა"]
        },
        "ლევან": {
            "ასაკი": 16,
            "საშუალო_ქულა": 6.8,
            "საგნები": {"მათემატიკა": {"ქულა": 5}, "ფიზიკა": {"ქულა": 7}},
            "დასწრება": 60,
            "დამატებითი": []
        }
    }
}

all_students = []

for class_name in students:
    for student_name in students[class_name]:
        # ვიღებთ სტუდენტის მონაცემებს
        info = students[class_name][student_name]

        # ვქმნით სრულიად ახალ ლექსიკონს
        temp_dict = {
            "სახელი": student_name,
            "კლასი": class_name,
            "საშუალო_ქულა": info["საშუალო_ქულა"],
            "დასწრება": info["დასწრება"],
            "საგნები": info["საგნები"],
            "დამატებითი": info["დამატებითი"]
        }
        all_students.append(temp_dict)



# 1. სახელი და საშუალო ქულა
for s in all_students:
    print(f"სტუდენტი: {s['სახელი']}, საშუალო ქულა: {s['საშუალო_ქულა']}")

# 2. საუკეთესო სტუდენტი
highest_grade = max(s['საშუალო_ქულა'] for s in all_students)
best_student_name = [s['სახელი'] for s in all_students if s['საშუალო_ქულა'] == highest_grade][0]
print(f"\nსაუკეთესო სტუდენტი: {best_student_name} ({highest_grade})")

# 3. დასწრება > 90%
high_attendance = [s['სახელი'] for s in all_students if s['დასწრება'] > 90]
print(f"მაღალი დასწრება: {high_attendance}")

# 4. კლასი ყველაზე მეტი სტუდენტით
class_counts = {}
for s in all_students:
    c_name = s['კლასი']
    class_counts[c_name] = class_counts.get(c_name, 0) + 1

max_acts = max(len(s['დამატებითი']) for s in all_students)
for s in all_students:
    if len(s['დამატებითი']) == max_acts:
        print(f"ყველაზე აქტიური სტუდენტი: {s['სახელი']}")
        break

# 5. ვინ დადის პროგრამირებაზე
programmers = [s['სახელი'] for s in all_students if "პროგრამირება" in s['დამატებითი']]
print(f"პროგრამირების სტუდენტები: {programmers}")

# 6. საშუალო დასწრება სკოლაში
avg_attendance = sum(s['დასწრება'] for s in all_students) / len(all_students)
print(f"საშუალო დასწრება სკოლაში: {avg_attendance}%")

# 7. ახალი ლექსიკონი (სახელი: საგნების რაოდენობა)
subject_counts = {s['სახელი']: len(s['საგნები']) for s in all_students}
print(f"საგნების რაოდენობა: {subject_counts}")

# 8. ყველაზე მეტი აქტივობა
active_student = max(all_students, key=lambda x: len(x['დამატებითი']))
print(f"ყველაზე აქტიური სტუდენტი: {active_student['სახელი']}")
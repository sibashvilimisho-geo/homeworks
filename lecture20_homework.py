import csv
import os
from datetime import datetime

CSV_FILE = "products.csv"
LOG_FILE = "log.txt"


# Log action
def log_action(username, action, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] USER={username} | ACTION={action}"
    if details:
        log_msg += f" | {details}"

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_msg + "\n")


# CSV
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "price", "stock"])


# 1.  show all products
def show_all_products(username):
    log_action(username, "VIEW_ALL_PRODUCTS")

    try:
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader, None)

            print("\n=== პროდუქტების სია ===")
            print(f"{'ID':<5} {'სახელი':<15} {'ფასი':<10} {'რაოდენობა':<10}")
            print("-" * 45)

            for row in reader:

                try:
                    print(f"{row[0]:<5} {row[1]:<15} {row[2]:<10} {row[3]:<10}")
                except IndexError:

                    continue

    except FileNotFoundError:

        print(f"❌ შეცდომა: ფაილი '{CSV_FILE}' ვერ მოიძებნა!")

# 2. Get product by ID
def get_product_by_id(username):
    prod_id = input("შეიყვანეთ პროდუქტის ID: ").strip()
    log_action(username, "GET_PRODUCT", f"PRODUCT_ID={prod_id}")

    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if row[0] == prod_id:
                print(f"\n✅ ნაპოვნია: ID: {row[0]} | სახელი: {row[1]} | ფასი: {row[2]} | რაოდენობა: {row[3]}")
                return

        print(f"\n❌ პროდუქტი ID-ით '{prod_id}' ვერ მოიძებნა.")


# 3. Add product
def add_product(username):
    name = input("შეიყვანეთ პროდუქტის სახელი: ").strip()
    price = input("შეიყვანეთ ფასი: ").strip()
    stock = input("შეიყვანეთ რაოდენობა: ").strip()

    max_id = 0
    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if row:
                try:

                    current_id = int(row[0])
                    max_id = max(max_id, current_id)
                except (ValueError, IndexError):

                    continue

    new_id = max_id + 1


    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([new_id, name, price, stock])

    log_action(username, "ADD_PRODUCT", f"NAME={name}")
    print(f"\n✅ პროდუქტი '{name}' წარმატებით დაემატა (ID: {new_id}).")


# 4. Delete product
def delete_product(username):
    prod_id = input("შეიყვანეთ წასაშლელი პროდუქტის ID: ").strip()

    rows = []
    found = False

    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        rows.append(header)

        for row in reader:
            if row[0] == prod_id:
                found = True
            else:
                rows.append(row)

    if found:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        log_action(username, "DELETE_PRODUCT", f"PRODUCT_ID={prod_id}")
        print(f"\n✅ პროდუქტი ID: {prod_id} წარმატებით წაიშალა.")
    else:
        log_action(username, "DELETE_PRODUCT_FAILED", f"PRODUCT_ID={prod_id}")
        print(f"\n❌ პროდუქტი ID-ით '{prod_id}' ვერ მოიძებნა.")


# მენიუ
def main():
    initialize_csv()

    print("=== პროდუქტების მართვის სისტემა ===")
    username = input("Enter your name: ").strip()
    if not username:
        username = "Anonymous"

    log_action(username, "LOGIN")

    while True:
        print("\n--- მენიუ ---")
        print("1. Show all products")
        print("2. Get product by id")
        print("3. Add product")
        print("4. Delete product")
        print("5. Exit")

        choice = input("აირჩიეთ მოქმედება (1-5): ").strip()

        if choice == "1":
            show_all_products(username)
        elif choice == "2":
            get_product_by_id(username)
        elif choice == "3":
            add_product(username)
        elif choice == "4":
            delete_product(username)
        elif choice == "5":
            log_action(username, "EXIT")
            print("\n👋 პროგრამა დასრულებულია. ნახვამდის!")
            break
        else:
            print("\n⚠️ არასწორი არჩევანი! გთხოვთ აირჩიოთ 1-დან 5-მდე.")


if __name__ == "__main__":
    main()
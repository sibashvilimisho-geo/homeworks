import os
from datetime import datetime
import pandas as pd

CSV_FILE = "products.csv"
LOG_FILE = "log.txt"

# Helping tools

def initialize_files():
    required_columns = ["id", "name", "price", "stock"]
    if os.path.exists(CSV_FILE):
        try:
            df = pd.read_csv(CSV_FILE)
            df.columns = df.columns.str.strip()
            if "id" not in df.columns:
                df = pd.DataFrame(columns=required_columns)
                df.to_csv(CSV_FILE, index=False)

        except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError):
            df = pd.DataFrame(columns=required_columns)
            df.to_csv(CSV_FILE, index=False)
    else:
        df = pd.DataFrame(columns=required_columns)
        df.to_csv(CSV_FILE, index=False)


def load_products():
    try:
        df = pd.read_csv(CSV_FILE)
        df.columns = df.columns.str.strip()
        return df

    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError):
        return pd.DataFrame(columns=["id", "name", "price", "stock"])


def save_products(df):

    df.to_csv(CSV_FILE, index=False)


def log_action(user, action, details=""):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{current_time}] USER={user} | ACTION={action}"
    if details:
        log_msg += f" | {details}"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_msg + "\n")



# Show all products
def show_all_products(user):

    df = load_products()
    log_action(user, "VIEW_ALL_PRODUCTS")

    if df.empty:
        print("\n📭 პროდუქტების სია ცარიელია.")
        return

    print("\n--- პროდუქტების სია ---")
    print(df.to_string(index=False))
    print("----------------------")

# Get product by ID

def get_product_by_id(user):

    try:
        prod_id = int(input("შემოიტანეთ პროდუქტის ID: "))
    except ValueError:
        print("❌ შეცდომა: ID უნდა იყოს მთელი რიცხვი!")
        return

    df = load_products()
    log_action(user, "GET_PRODUCT", f"PRODUCT_ID={prod_id}")

    result = df[df["id"] == prod_id]

    if not result.empty:
        print("\n🔍 მოიძებნა პროდუქტი:")
        print(result.to_string(index=False))
    else:
        print(f"❌ პროდუქტი ID-ით [{prod_id}] ვერ მოიძებნა.")

# Add product

def add_product(user):

    df = load_products()

    try:
        name = input("შეიყვანეთ პროდუქტის სახელი: ").strip()
        if not name:
            print("❌ სახელი არ უნდა იყოს ცარიელი!")
            return

        price = float(input("შეიყვანეთ ფასი: "))
        stock = int(input("შეიყვანეთ რაოდენობა: "))

        if price < 0 or stock < 0:
            print("❌ ფასი და რაოდენობა არ შეიძლება იყოს უარყოფითი!")
            return

        next_id = int(df["id"].max() + 1) if not df.empty else 1

        new_row = {
            "id": next_id,
            "name": name,
            "price": price,
            "stock": stock,
        }


        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        save_products(df)
        log_action(user, "ADD_PRODUCT", f"NAME={name}")
        print(f"✅ პროდუქტი '{name}' წარმატებით დაემატა (ID: {next_id})!")

    except ValueError:
        print("❌ შეცდომა: არავალიდური ფასი ან რაოდენობა!")

# Delete product

def delete_product(user):

    try:
        prod_id = int(input("შემოიტანეთ წასაშლელი პროდუქტის ID: "))
    except ValueError:
        print("❌ შეცდომა: ID უნდა იყოს მთელი რიცხვი!")
        return

    df = load_products()

    if prod_id in df["id"].values:

        df = df[df["id"] != prod_id]
        save_products(df)

        log_action(user, "DELETE_PRODUCT", f"PRODUCT_ID={prod_id}")
        print(f"❌ პროდუქტი ID-ით [{prod_id}] წარმატებით წაიშალა.")
    else:
        print(f"❌ პროდუქტი ID-ით [{prod_id}] ვერ მოიძებნა.")


# --- მთავარი მენიუ ---


def main():
    initialize_files()

    print("=== პროდუქტების მართვის სისტემა ===")
    user_name = input("Enter your name: ").strip()

    if not user_name:
        user_name = "Guest"

    while True:
        print("\n--- MENU ---")
        print("1. Show all products")
        print("2. Get product by id")
        print("3. Add product")
        print("4. Delete product")
        print("5. Exit")

        choice = input("აირჩიეთ მოქმედება (1-5): ").strip()

        if choice == "1":
            show_all_products(user_name)
        elif choice == "2":
            get_product_by_id(user_name)
        elif choice == "3":
            add_product(user_name)
        elif choice == "4":
            delete_product(user_name)
        elif choice == "5":
            print(f"👋 ნახვამდის, {user_name}!")
            break
        else:
            print("⚠️ არასწორი არჩევანი. გთხოვთ შეიყვანოთ რიცხვი 1-დან 5-მდე.")


if __name__ == "__main__":
    main()
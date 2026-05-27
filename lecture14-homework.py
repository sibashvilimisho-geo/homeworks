import os

def count_file_metrics(filename="data.txt"):

    print(f"\n--- Task 1: Word Counter ({filename}) ---")
    try:

        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as f:
                f.write("Hello, this is the first line.\nThis is the second line.\nGood luck with programming!")
            print(f"Notice: {filename} did not exist, a sample file was created.")

        lines_count = 0
        words_count = 0
        chars_count = 0

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                lines_count += 1
                chars_count += len(line)
                words = line.split()
                words_count += len(words)

        print(f"Lines:      {lines_count}")
        print(f"Words:      {words_count}")
        print(f"Characters: {chars_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def manage_journal(filename="journal.txt"):

    print(f"\n--- Task 2: Records Journal ({filename}) ---")
    print("Enter your logs. Type 'exit' to end the program.")

    while True:
        try:
            user_input = input("Log entry: ").strip()

            if user_input.lower() == 'exit':
                print("Journal writing completed.")
                break

            if not user_input:
                print("Empty entries will not be saved. Please try again.")
                continue


            with open(filename, "a", encoding="utf-8") as file:
                file.write(user_input + "\n")
            print("-> Entry successfully added.")

        except IOError:
            print("Error: An I/O error occurred while writing to the file.")
        except Exception as e:
            print(f"An error occurred: {e}")


import csv


def create_sample_products_csv(filename="products.csv"):

    products = [
        {"product_name": "Laptop", "price": "1500"},
        {"product_name": "Phone", "price": "800"},
        {"product_name": "Headphones", "price": "150"},
        {"product_name": "Mouse", "price": "50"},
        {"product_name": "Monitor", "price": "450"}
    ]
    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["product_name", "price"])
            writer.writeheader()
            writer.writerows(products)
    except Exception as e:
        print(f"Failed to create sample product CSV: {e}")


def filter_products_by_price(input_file="products.csv", output_file="filtered_products.csv"):

    print(f"\n--- Task 3: CSV Filter ({input_file} -> {output_file}) ---")

    if not os.path.exists(input_file):
        create_sample_products_csv(input_file)
        print(f"Notice: Created a sample file '{input_file}' since it wasn't found.")

    try:
        min_price_input = input("Enter minimum price: ").strip()
        min_price = float(min_price_input)
    except ValueError:
        print("Error: Invalid price entered. Please input a valid number.")
        return

    try:
        filtered_products = []
        with open(input_file, "r", encoding="utf-8") as infile:
            reader = csv.DictReader(infile)

            if "price" not in reader.fieldnames:
                print("Error: CSV file missing the required 'price' column.")
                return

            for row in reader:
                try:
                    current_price = float(row["price"])
                    if current_price > min_price:
                        filtered_products.append(row)
                except ValueError:

                    continue


        with open(output_file, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames or [])
            writer.writeheader()
            if filtered_products:
                writer.writerows(filtered_products)

        print(f"Filtering complete. Found {len(filtered_products)} product(s). Saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The input file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred during filtering: {e}")


def initialize_contacts_file(filename="contacts.csv"):

    if not os.path.exists(filename):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "phone", "email"])
        except Exception as e:
            print(f"Error initializing contact file: {e}")


def view_all_contacts(filename="contacts.csv"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            contacts = list(reader)

            if not contacts:
                print("\nYour contacts book is currently empty.")
                return

            print("\n--- Contact List ---")
            for idx, contact in enumerate(contacts, 1):
                print(
                    f"{idx}. Name: {contact.get('name')}, Phone: {contact.get('phone')}, Email: {contact.get('email')}")
    except Exception as e:
        print(f"Error reading contacts: {e}")


def add_contact(filename="contacts.csv"):
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()

    if not name:
        print("Error: Contact name cannot be empty.")
        return

    try:
        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name, phone, email])
        print(f"Contact '{name}' added successfully.")
    except Exception as e:
        print(f"Error saving contact: {e}")


def search_contact(filename="contacts.csv"):
    print("\n--- Search Contact ---")
    search_name = input("Enter name to search (partial matches allowed): ").strip().lower()

    if not search_name:
        print("Search term cannot be empty.")
        return

    try:
        found = False
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if search_name in row["name"].lower():
                    print(f"Found -> Name: {row['name']}, Phone: {row['phone']}, Email: {row['email']}")
                    found = True
        if not found:
            print("No matching contact found.")
    except Exception as e:
        print(f"An error occurred while searching: {e}")


def delete_contact(filename="contacts.csv"):
    print("\n--- Delete Contact ---")
    target_name = input("Enter the exact name of the contact to delete: ").strip()

    if not target_name:
        print("Name cannot be empty.")
        return

    try:
        updated_rows = []
        found = False

        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            for row in reader:
                if row["name"].lower() == target_name.lower():
                    found = True  # Match found, skip adding to exclude it (delete)
                else:
                    updated_rows.append(row)

        if not found:
            print(f"Notification: Contact with name '{target_name}' was not found.")
            return

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames or [])
            writer.writeheader()
            writer.writerows(updated_rows)

        print(f"Contact '{target_name}' deleted successfully.")

    except Exception as e:
        print(f"An error occurred during deletion: {e}")


def manage_contacts_book():
    filename = "contacts.csv"
    initialize_contacts_file(filename)

    while True:
        print("\n======= Task 4: Contacts Book =======")
        print("1. View All Contacts")
        print("2. Add Contact")
        print("3. Search Contact by Name")
        print("4. Delete Contact")
        print("5. Return to Main Menu")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            view_all_contacts(filename)
        elif choice == "2":
            add_contact(filename)
        elif choice == "3":
            search_contact(filename)
        elif choice == "4":
            delete_contact(filename)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")


import random


def generate_fake_data_demo():

    print("\n--- 🌟 Optional Task: Faker and Random Demo ---")


    random_score = random.randint(50, 95)
    print(f"Random integer generated between 50 and 95: {random_score}")


    try:
        from faker import Faker

        fake = Faker()
        print("Fake realistic data generated via Faker library:")
        print(f"Name:    {fake.name()}")
        print(f"Email:   {fake.email()}")
        print(f"Address: {fake.address()}")
    except ImportError:
        print("Notice: 'faker' library is not installed (run: pip install faker).")
        print("Fallback mock data generated using random:")
        names = ["John Doe", "Anna Smith", "Michael Jordan"]
        addresses = ["New York, Wall St 12", "London, Baker St 221B"]
        print(f"Name:    {random.choice(names)}")
        print(f"Email:   user{random.randint(10, 99)}@example.com")
        print(f"Address: {random.choice(addresses)}")


def main():
    while True:
        print("\n==========================================")
        print("                MAIN MENU                 ")
        print("==========================================")
        print("1. Task 1 — Word Counter (data.txt)")
        print("2. Task 2 — Records Journal (journal.txt)")
        print("3. Task 3 — CSV Filter (products.csv)")
        print("4. Task 4 — Contacts Book (contacts.csv)")
        print("5. Optional Task — Faker & Random Demo")
        print("6. Exit")
        print("==========================================")

        choice = input("Select a task number (1-6): ").strip()

        if choice == "1":
            count_file_metrics()
        elif choice == "2":
            manage_journal()
        elif choice == "3":
            filter_products_by_price()
        elif choice == "4":
            manage_contacts_book()
        elif choice == "5":
            generate_fake_data_demo()
        elif choice == "6":
            print("Thank you! Program closed safely.")
            break
        else:
            print("Invalid choice, please select an option from 1 to 6.")


if __name__ == "__main__":
    main()
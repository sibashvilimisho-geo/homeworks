import json
import os
from dataclasses import asdict, dataclass


# Step 1 — Model
@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    available: bool


# Step 2 — JSON Operations
def save_books(books):
    with open("books.json", "w", encoding="utf-8") as f:
        json.dump([asdict(b) for b in books], f, ensure_ascii=False, indent=2)


def load_books():
    if os.path.exists("books.json"):
        with open("books.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book(**item) for item in data]
    return []


# Step 4 — Core Functional Requirements
def add_book(books):
    print("\n--- Add a New Book ---")
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()

    while True:
        try:
            year = int(input("Enter year: "))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number for the year.")

    new_id = max((b.id for b in books), default=0) + 1
    new_book = Book(
        id=new_id, title=title, author=author, year=year, available=True
    )
    books.append(new_book)
    print(f"✅ Book added successfully! (ID: {new_id})")


def view_all_books(books):
    print("\n--- Library Catalog ---")
    if not books:
        print("The library is currently empty.")
        return

    for b in books:
        status = "Available" if b.available else "Borrowed"
        print(f"ID: {b.id} | {b.title} | {b.author} | {b.year} | {status}")


def search_by_title(books):
    print("\n--- Search Books ---")
    query = input("Enter title to search for: ").strip().lower()

    found_books = [b for b in books if query in b.title.lower()]

    if not found_books:
        print("❌ No books matched your search query.")
        return

    print(f"\nFound {len(found_books)} matching result(s):")
    for b in found_books:
        status = "Available" if b.available else "Borrowed"
        print(f"ID: {b.id} | {b.title} | {b.author} | {b.year} | {status}")


def borrow_book(books):
    print("\n--- Borrow a Book ---")
    try:
        book_id = int(input("Enter Book ID to borrow: "))
    except ValueError:
        print("❌ Invalid ID format. Please enter a number.")
        return

    for b in books:
        if b.id == book_id:
            if b.available:
                b.available = False
                print(f"✅ Success! You have borrowed '{b.title}'.")
            else:
                print(
                    f"❌ Error: '{b.title}' is already borrowed by someone else."
                )
            return

    print("❌ Error: Book with that ID was not found.")


def return_book(books):
    print("\n--- Return a Book ---")
    try:
        book_id = int(input("Enter Book ID to return: "))
    except ValueError:
        print("❌ Invalid ID format. Please enter a number.")
        return

    for b in books:
        if b.id == book_id:
            if not b.available:
                b.available = True
                print(f"✅ Success! '{b.title}' has been returned to shelves.")
            else:
                print(f"ℹ️ Info: '{b.title}' is already marked as available.")
            return

    print("❌ Error: Book with that ID was not found.")


def display_statistics(books):
    print("\n--- Library Statistics ---")
    total_books = len(books)
    available_books = sum(1 for b in books if b.available)
    borrowed_books = total_books - available_books

    print(f"Total books:      {total_books}")
    print(f"Available:        {available_books}")
    print(f"Borrowed:         {borrowed_books}")


# Step 3 — Main Application Interface
def main():
    books = load_books()

    while True:
        print("\n==============================")
        print("  Library Management System   ")
        print("==============================")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book by Title")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Statistics")
        print("7. Save Progress")
        print("8. Exit")
        print("==============================")

        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_all_books(books)
        elif choice == "3":
            search_by_title(books)
        elif choice == "4":
            borrow_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            display_statistics(books)
        elif choice == "7":
            save_books(books)
            print("💾 Data saved successfully to 'books.json'.")
        elif choice == "8":

            save_books(books)
            print("\n💾 Progress saved automatically. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please choose a option between 1 and 8.")


if __name__ == "__main__":
    main()
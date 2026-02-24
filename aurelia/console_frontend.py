# test_frontend.py
"""
Aurelia Console-Based Front End
Full CRUD for:
- Users
- Dreams
- Symbols
- Poems
- DreamSymbols

Includes:
✔ Input validation
✔ Error handling
✔ Read-all verification after changes
"""

import requests
from pprint import pprint

BASE_URL = "http://127.0.0.1:8000"


# ==========================
# HELPER FUNCTIONS
# ==========================

def get_int(prompt):
    """Validate integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_non_empty(prompt):
    """Ensure non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def safe_request(method, endpoint, data=None):
    try:
        url = f"{BASE_URL}{endpoint}"
        if method == "GET":
            r = requests.get(url)
        elif method == "POST":
            r = requests.post(url, json=data)
        elif method == "PUT":
            r = requests.put(url, json=data)
        elif method == "DELETE":
            r = requests.delete(url)
        else:
            return None

        if r.status_code >= 400:
            print(f"Error {r.status_code}: {r.text}")
            return None

        if r.text:
            return r.json()
        return None

    except Exception as e:
        print("Request failed:", e)
        return None


def print_all(endpoint):
    data = safe_request("GET", endpoint)
    if data is not None:
        pprint(data)


# ==========================
# USERS MENU
# ==========================

def users_menu():
    while True:
        print("\n--- USERS MENU ---")
        print("1. Create")
        print("2. View All")
        print("3. Update")
        print("4. Delete")
        print("5. Back")

        choice = input("Select option: ")

        if choice == "1":
            name = get_non_empty("Name: ")
            email = get_non_empty("Email: ")
            safe_request("POST", "/users", {"name": name, "email": email})
            print_all("/users")

        elif choice == "2":
            print_all("/users")

        elif choice == "3":
            user_id = get_int("User ID to update: ")
            name = get_non_empty("New Name: ")
            email = get_non_empty("New Email: ")
            safe_request("PUT", f"/users/{user_id}", {"name": name, "email": email})
            print_all("/users")

        elif choice == "4":
            user_id = get_int("User ID to delete: ")
            safe_request("DELETE", f"/users/{user_id}")
            print_all("/users")

        elif choice == "5":
            break


# ==========================
# DREAMS MENU
# ==========================

def dreams_menu():
    while True:
        print("\n--- DREAMS MENU ---")
        print("1. Create")
        print("2. View All")
        print("3. Update")
        print("4. Delete")
        print("5. Back")

        choice = input("Select option: ")

        if choice == "1":
            user_id = get_int("User ID: ")
            title = get_non_empty("Title: ")
            description = get_non_empty("Description: ")
            date = get_non_empty("Date (YYYY-MM-DD): ")
            mood = get_non_empty("Mood: ")
            vividness = get_int("Vividness (1-10): ")

            safe_request("POST", "/dreams", {
                "user_id": user_id,
                "title": title,
                "description": description,
                "date": date,
                "mood": mood,
                "vividness": vividness
            })
            print_all("/dreams")

        elif choice == "2":
            print_all("/dreams")

        elif choice == "3":
            dream_id = get_int("Dream ID: ")
            user_id = get_int("User ID: ")
            title = get_non_empty("Title: ")
            description = get_non_empty("Description: ")
            date = get_non_empty("Date: ")
            mood = get_non_empty("Mood: ")
            vividness = get_int("Vividness: ")

            safe_request("PUT", f"/dreams/{dream_id}", {
                "user_id": user_id,
                "title": title,
                "description": description,
                "date": date,
                "mood": mood,
                "vividness": vividness
            })
            print_all("/dreams")

        elif choice == "4":
            dream_id = get_int("Dream ID to delete: ")
            safe_request("DELETE", f"/dreams/{dream_id}")
            print_all("/dreams")

        elif choice == "5":
            break


# ==========================
# SYMBOLS MENU
# ==========================

def symbols_menu():
    while True:
        print("\n--- SYMBOLS MENU ---")
        print("1. Create")
        print("2. View All")
        print("3. Update")
        print("4. Delete")
        print("5. Back")

        choice = input("Select option: ")

        if choice == "1":
            name = get_non_empty("Name: ")
            description = get_non_empty("Description: ")
            safe_request("POST", "/symbols", {"name": name, "description": description})
            print_all("/symbols")

        elif choice == "2":
            print_all("/symbols")

        elif choice == "3":
            symbol_id = get_int("Symbol ID: ")
            name = get_non_empty("New Name: ")
            description = get_non_empty("New Description: ")
            safe_request("PUT", f"/symbols/{symbol_id}",
                         {"name": name, "description": description})
            print_all("/symbols")

        elif choice == "4":
            symbol_id = get_int("Symbol ID to delete: ")
            safe_request("DELETE", f"/symbols/{symbol_id}")
            print_all("/symbols")

        elif choice == "5":
            break


# ==========================
# POEMS MENU
# ==========================

def poems_menu():
    while True:
        print("\n--- POEMS MENU ---")
        print("1. Create")
        print("2. View All")
        print("3. Update")
        print("4. Delete")
        print("5. Back")

        choice = input("Select option: ")

        if choice == "1":
            author_id = get_int("Author ID: ")
            dream_id = get_int("Dream ID: ")
            content = get_non_empty("Content: ")
            created_at = get_non_empty("Created Date (YYYY-MM-DD): ")

            safe_request("POST", "/poems", {
                "author_id": author_id,
                "dream_id": dream_id,
                "content": content,
                "created_at": created_at
            })
            print_all("/poems")

        elif choice == "2":
            print_all("/poems")

        elif choice == "3":
            poem_id = get_int("Poem ID: ")
            author_id = get_int("Author ID: ")
            dream_id = get_int("Dream ID: ")
            content = get_non_empty("Content: ")
            created_at = get_non_empty("Created Date: ")

            safe_request("PUT", f"/poems/{poem_id}", {
                "author_id": author_id,
                "dream_id": dream_id,
                "content": content,
                "created_at": created_at
            })
            print_all("/poems")

        elif choice == "4":
            poem_id = get_int("Poem ID to delete: ")
            safe_request("DELETE", f"/poems/{poem_id}")
            print_all("/poems")

        elif choice == "5":
            break


# ==========================
# DREAM SYMBOLS MENU
# ==========================

def dreamsymbols_menu():
    while True:
        print("\n--- DREAM SYMBOLS MENU ---")
        print("1. Link Symbol to Dream")
        print("2. View All Links")
        print("3. Unlink Symbol from Dream")
        print("4. Back")

        choice = input("Select option: ")

        if choice == "1":
            dream_id = get_int("Dream ID: ")
            symbol_id = get_int("Symbol ID: ")

            safe_request("POST", "/dreamsymbols", {
                "dream_id": dream_id,
                "symbol_id": symbol_id
            })
            print_all("/dreamsymbols")

        elif choice == "2":
            print_all("/dreamsymbols")

        elif choice == "3":
            dream_id = get_int("Dream ID: ")
            symbol_id = get_int("Symbol ID: ")
            safe_request("DELETE", f"/dreamsymbols?dream_id={dream_id}&symbol_id={symbol_id}")
            print_all("/dreamsymbols")

        elif choice == "4":
            break


# ==========================
# MAIN MENU
# ==========================

def main():
    print("=== Aurelia Console Front End ===")

    while True:
        print("\nMAIN MENU")
        print("1. Users")
        print("2. Dreams")
        print("3. Symbols")
        print("4. Poems")
        print("5. DreamSymbols")
        print("6. Exit")

        choice = input("Select option: ")

        if choice == "1":
            users_menu()
        elif choice == "2":
            dreams_menu()
        elif choice == "3":
            symbols_menu()
        elif choice == "4":
            poems_menu()
        elif choice == "5":
            dreamsymbols_menu()
        elif choice == "6":
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
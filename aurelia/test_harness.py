from app.data.data_provider import DataProvider

def print_users(dp):
    print("\n--- USERS ---")
    users = dp.read_all_users()
    for u in users:
        print(f"[{u['id']}] {u['name']} <{u['email']}>")

def print_dreams(dp):
    print("\n--- DREAMS ---")
    dreams = dp.read_all_dreams()
    for d in dreams:
        print(f"[{d['id']}] User {d['user_id']} | {d['title']} | {d['mood']} | Vividness: {d['vividness']}")

def print_symbols(dp):
    print("\n--- SYMBOLS ---")
    symbols = dp.read_all_symbols()
    for s in symbols:
        print(f"[{s['id']}] {s['name']} - {s['description']}")

def print_poems(dp):
    print("\n--- POEMS ---")
    poems = dp.read_all_poems()
    for p in poems:
        print(f"[{p['id']}] Author {p['author_id']} | Dream {p['dream_id']}")
        print(f"    {p['content']}")

def main():
    print("=== Aurelia Console Test Harness ===")

    dp = DataProvider()

    while True:
        print("\nMenu:")
        print("1. View all users")
        print("2. View all dreams")
        print("3. View all symbols")
        print("4. View all poems")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print_users(dp)
        elif choice == "2":
            print_dreams(dp)
        elif choice == "3":
            print_symbols(dp)
        elif choice == "4":
            print_poems(dp)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
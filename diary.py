
import datetime

FILENAME = "notes.txt"

def write_entry():
    note = input("\nEnter your diary note: ")
    with open(FILENAME, "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {note}\n")
    print("Note saved.\n")

def view_entries():
    print("\n--- Diary Entries ---")
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            content = f.read()
            if content:
                print(content)
            else:
                print("No entries yet.")
    except FileNotFoundError:
        print("No diary found yet.")

def main():
    while True:
        print("\n1. Write Entry\n2. View Entries\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

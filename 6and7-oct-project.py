#project6
#File operator
from datetime import datetime
class journalmanager:
    def __init__(self):
        self.filename="journal.txt"
    def add_entry(self):
        data=input("Write your journal entry:")
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.filename,"a") as f:
                f.write(f"{time}-{data}\n")
            print("Entry added successfully")
        except Exception as e:
            print("Error:",e)
    def view_entries(self):
        try:
            with open(self.filename,"r") as f:
                data= f.read().strip()
                if data:
                    print("Your journal entries")
                    print("-"*30)
                    print(data)
                    print()
                else:
                    print("No entries found")
        except Exception as e:
            print("Error",e)
    def search_entry(self):
        try:
            keyword=input("Enter a keyword to search:").lower()
            with open(self.filename,"r") as f:
                entries = f.read().split("\n\n")
            found = False
            for entry in entries:
                if keyword in entry.lower():
                    print(entry)
                    print("-"*30)
                    found = True
                else:
                    print("No entries found for the keyword:", keyword, "\n")
        except Exception as e:
            print("Error:",e)
    def delete_entries(self):
            confirm=input("Are your sure that you want to delete all entires?(yes/no):")
            if confirm.lower() =="yes":
                try:
                    open(self.filename,"w").close()
                    print("All entries deleted successfully")
                except Exception as e:
                    print("Error:",e)
            else:
                print("Deletion cancelled.\n")
journal= journalmanager()
while True:
    print()
    print("Welcome to Personal Journal Manager")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search for an entry")
    print("4. Delete all entries")
    print("5. Exit")
    choice=input("Enter your choice:").strip()
    match choice:
        case "1":
            journal.add_entry()
        case "2":
            journal.view_entries()
        case "3":
            journal.search_entry()
        case "4":
            journal.delete_entries()
        case "5":
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        case _:
            print("Invalid choice. Please select a valid option from the menu.")






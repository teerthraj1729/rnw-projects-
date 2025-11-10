#Project 7
#modular and packages
import time
from mutli_utility_toolkit.multitoolkit import (
    current_datetime, diff_between_dates, format_date, stopwatch, countdown,
    factorial, compound_interest, area_circle, trig_values,
    random_number, random_list, random_password, generate_otp,
    generate_uuid4, create_file, write_file, read_file, append_file,
    list_module_attributes
)
def datetime_menu():
    while True:
        print()
        print("Datetime and time operations:")
        print("1. Display current time and date")
        print("2. Calculate difference between dates/times")
        print("3. Format data into custom format")
        print("4. Stopwatch ")
        print("5. Countdown timer")
        print("6. Back to main menu")
        ch1 = input("Enter your choice:").strip()
        match ch1:
            case "1":
                print("Current Date and Time:", current_datetime())
            case "2":
                a = input("Enter the first date (YYYY-MM-DD): ").strip()
                b = input("Enter the second date (YYYY-MM-DD): ").strip()
                print("Difference:", diff_between_dates(a, b), "days")
            case "3":
                d = input("Enter date (YYYY-MM-DD): ").strip()
                print("Formatted:", format_date(d))
            case "4":
                sec = float(input("Enter seconds to run stopwatch demo: ").strip() or "0")
                elapsed = stopwatch(sec)
                print(f"Elapsed (approx): {elapsed:.2f} seconds")
            case "5":
                sec = int(input("Enter countdown seconds: ").strip() or "3")
                for s in countdown(sec):
                    print(s)
                    time.sleep(1)
                print("Done!")
            case "6":
                break
            case _:
                print("Invalid choice. Please try again!")
def math_menu():
    while True:
        print()
        print("Mathematical Operations:")
        print("1. Calculate factorial")
        print("2. Solve compound interest")
        print("3. Trignometric calculations")
        print("4. Area of geometric shapes")
        print("5. Back to main menu")
        ch2 = input("Enter your choice:").strip()
        match ch2:
            case "1":
                n = int(input("Enter a non-negative integer: ").strip())
                print("Factorial:", factorial(n))
            case "2":
                p = float(input("Principal amount: ").strip())
                r = float(input("Rate (%) : ").strip())
                t = float(input("Time (years): ").strip())
                print("Amount:", compound_interest(p, r, t))
            case "3":
                x = float(input("Enter angle in radians: ").strip())
                print("Trigonometric:", trig_values(x))
            case "4":
                r = float(input("Radius: ").strip())
                print("Area:", area_circle(r))
            case "5":
                break
            case _:
                print("Invalid choice. Please try again!")
def random_menu():
    while True:
        print()
        print("Random data generation:")
        print("1. Genrate random number")
        print("2. Genrate random list")
        print("3. Create random password")
        print("4. Generate random OTP")
        print("5. Back to main menu")
        ch3 = input("Enter your choice:").strip()
        match ch3:
            case "1":
                low = int(input("Low: ").strip() or "0")
                high = int(input("High: ").strip() or "100")
                print("Random Number:", random_number(low, high))
            case "2":
                n = int(input("Length of list: ").strip() or "5")
                print("Random List:", random_list(n))
            case "3":
                l = int(input("Password length: ").strip() or "8")
                print("Generated Password:", random_password(l))
            case "4":
                print("Generated OTP:", generate_otp())
            case "5":
                break
            case _:
                print("Invalid choice. Please try again!")
def uuid_menu():
    print("\nGenerate Unique Identifier (UUID4):")
    print("Generated UUID:", generate_uuid4())

def file_menu():
    while True:
        print()
        print("File operations:")
        print("1. Create a new file")
        print("2. Write a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to main menu")
        ch4 = input("Enter your choice:").strip()
        match ch4:
            case "1":
                name = input("Enter file name: ").strip()
                create_file(name)
                print("File created successfully!")
            case "2":
                name = input("Enter file name: ").strip()
                data = input("Enter data to write: ")
                write_file(name, data + "\n")
                print("Data written successfully!")
            case "3":
                name = input("Enter file name: ").strip()
                try:
                    print("File Content:\n" + read_file(name))
                except FileNotFoundError as e:
                    print(e)
            case "4":
                name = input("Enter file name: ").strip()
                data = input("Enter data to append: ")
                append_file(name, data + "\n")
                print("Data appended successfully!")
            case "5":
                break
            case _:
                print("Invalid choice. Please try again!")
def explore_menu():
    print("\nExplore Module Attributes (dir()):")
    mod = input("Enter module name to explore (e.g., math): ").strip()
    try:
        attrs = list_module_attributes(mod)
        print("Available Attributes in", mod, ":\n", attrs[:50], "...\n(total:", len(attrs), ")")
    except Exception as e:
        print("Error:", e)
def  main_menu():
    while True:
        print()
        print("Welcome to Multi-Uility toolkit")
        print()
        print("Choose an option:")
        print("1. Datetime and time operations")
        print("2. Mathematical operations")
        print("3. Random data operations")
        print("4. Generate unique identifiers (UUID)")
        print("5. File operations (custom module)")
        print("6. Explore modular attributes (dir())")
        print("7. Exit")
        choice = input("Enter your choice:").strip()
        match choice:
            case "1":
                datetime_menu()
            case "2":
                math_menu()
            case "3":
                random_menu()
            case "4":
                uuid_menu()
            case "5":
                file_menu()
            case "6":
                explore_menu()
            case "7":
                print("Thank you for using the Multi-utility toolkit!")
            case _:
                print("Invalid choice. Please try again!")
if __name__ == "__main__":
    main_menu()

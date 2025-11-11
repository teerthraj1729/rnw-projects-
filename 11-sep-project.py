print("Welcome to the Pattern Generator and Number Analyzer")
print()
print("Select an option:")
print("1. Generate a pattern")
print("2. Analyze a range of numbers")
print("3. Exit")
print()
choice = int(input("Enter your choice:"))
print()
match choice :
     case 1:
        rows=int(input("Enter the number of rows for the pattern:"))
        print("Pattern is:")
        for i in range (1,rows+1):
             print("*" * i)        
     case 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        total = 0
        for num in range(start, end + 1):
            if num % 2 == 0:
                print("Number",num,"is Even")
            else:
                print("Number",num,"is Odd")
            total += num
        print("Sum of all numbers from",start, "to",end,"is",total)  
     case 3:print("Exiting the program. Goodbye!")
     case _:print("Invalid choice,try again!!")
print()     
print("Thank you, for using the Pattern Generator and Number Analyzer!")

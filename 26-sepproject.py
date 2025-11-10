data_list=[]
while True:
    print("Welcome to the Data Analyzer And Transformer Program")
    print()
    print("Main menu:")
    print("1. Input data")
    print("2. Display data summary(Built-in functions)")
    print("3. Calculate factorial(Recursion)")
    print("4. Filter Data by Threshold(Lambda function)")
    print("5. Sort Data ")
    print("6. Display Data Statistics")
    print("7. Exit Program")
    print()
    choice = int(input("Please enter your choice:"))
    match choice:
        case 1:
            data_list
            try:
                data_srt = input("Enter data (numbers separated by spaces):")
                data_list = [int(x) for x in data_srt.split()]
                print("Data stored successfully!")
            except ValueError:
                print("Error: Please enter valid numbers.")
        case 2:
            if not data_list:
                print("Data list is empty. Load data first.")
            else:
                print("\n--- Data Summary (Built-in Functions) ---")
                total_elements = len(data_list)
                sum_values = sum(data_list)
                average = sum_values / total_elements
                print(f"Total elements:",total_elements)
                print(f"Minimum value:",min(data_list))
                print(f"Maximum value:",max(data_list))
                print(f"Sum of all values:",sum_values)
                print(f"Average value:{average:.2f}")
        case 3:
            print("\n---Calculate Factorial(recursion)---" )
            try:
                num_str = input("Enter a non-negative integer: ")
                num = int(num_str)
                if num < 0:
                    print("Factorial is only defined for non-negative integers.")
                else:
                    factorial = 1
                    for i in range(1, num + 1):
                        factorial = factorial * i
                        print(f"The factorial of {num} is: {factorial}")
            except ValueError:
                print("Error: Invalid input. Please enter a whole number.")
                if __name__ == "__main__":
                    calculate_factorial()
        case 4:
            print("\n---Filter data by threshold(lambda funcation)---")
            if not data_list:
                print("Data list is empty. Load data first.")
            else:
                try:
                    threshold = int(input("Enter a threshold value to filter out data above this value: "))
                    filtered_list = list(filter(lambda x: x >= threshold, data_list))
                    print(f"Filtered Data (values >= {threshold}): {filtered_list}")
                except ValueError:
                    print("Error: Please enter a valid integer.")
        case 5:
            print("\n--- Sort Data ---")
            print("1. Ascending")
            print("2. Descending")
            s = int(input("Enter your choice (1 or 2): "))
            if s==1:
                data_list.sort
                print("Data sorted in Ascending Order.",data_list)
            else:
                data_list.sort(reverse=True)
                print("Data sorted in Descending Order.",data_list)
                    
                     
                         
        case 6:
            if not data_list:
                print("None")
            else:
                minimum = min(data_list)
                maximum = max(data_list)
                total_sum = sum(data_list)
                average = total_sum / len(data_list)
                print(f"Minimum value:",minimum)
                print(f"Maximum value:",maximum)
                print(f"Sum of values:",total_sum)
                print(f"Average value:",average)
        case 7:
            print("\n Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        case _:
            print("Invalid Choice. Try again!")

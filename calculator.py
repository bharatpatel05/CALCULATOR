def simple_calculator():
    print("4 Hey there! Welcome to the Simple Calculator!")

    try:
        num1 = float(input(" Enter your first number: "))
        num2 = float(input(" Enter your second number: "))
    except ValueError:
        print(" Oops! That doesn't look like a number. Please try again.")
        return

    print("\nWhat would you like to do?")
    print("1️ Add (+)")
    print("2️ Subtract (-)")
    print("3️ Multiply (*)")
    print("4️ Divide (/)")
    
    choice = input(" Choose an option (1/2/3/4): ")

    # Perform calculation
    if choice == '1':
        result = num1 + num2
        print(f"\n {num1} plus {num2} is {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"\n {num1} minus {num2} is {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"\n {num1} times {num2} is {result}")
    elif choice == '4':
        if num2 == 0:
            print(" You can't divide by zero! Try again with a different number.")
            return
        result = num1 / num2
        print(f"\n {num1} divided by {num2} is {result}")
    else:
        print(" Hmm... that wasn't a valid choice. Please run the program again.")

# Run the calculator
simple_calculator()

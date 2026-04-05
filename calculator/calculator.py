while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("Bye!")
        break

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if choice == "1":
        print("Answer:", num1 + num2)

    elif choice == "2":
        print("Answer:", num1 - num2)

    elif choice == "3":
        print("Answer:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Answer:", num1 / num2)

    else:
        print("Wrong choice")
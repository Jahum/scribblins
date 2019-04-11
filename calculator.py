def userInput():
    print("Enter the first number ");
    firstNumber=float(input());
    print("Enter the operator ");
    operation=input();
    print("Enter the second number ");
    secondNumber=float(input());
    if operation == "+":
        print(firstNumber+secondNumber);
    elif operation == "-":
        print(firstNumber-secondNumber);
    elif operation == "*":
        print(firstNumber*secondNumber);
    elif operation == "/":
        print(firstNumber/secondNumber);
    else:
        print ("Operation was not a valid character. Use + - * or /");
    return
userInput();
import Module as ADD

def main():
    firstNumber = int(input("Enter first number"))
    secondNumber = int(input("Enter second number"))

    result = ADD.addition(firstNumber, secondNumber) 
    print("Addition is: ", result)

if __name__ == "__main__":
    main()

from Module import addition

def main():
    firstNumber = int(input("Enter first number"))
    secondNumber = int(input("Enter second number"))

    result = addition(firstNumber, secondNumber) 
    result = substration(firstNumber, secondNumber) # Error
    print("Addition is: ", result)
    print("Substraction is: ", result)

if __name__ == "__main__":
    main()

# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def addition(firstNumber, secondNumber):
    return firstNumber + secondNumber

def substraction(firstNumber, secondNumber):
    return firstNumber - secondNumber

def multiplication(firstNumber, secondNumber):
    return firstNumber * secondNumber

def division(firstNumber, secondNumber):
    return firstNumber // secondNumber
    
def main():
    firstNumber = int(input("Enter first number"))
    secondNumber = int(input("Enter second number"))

    additionResult = addition(firstNumber, secondNumber)
    print("Addition is: ", additionResult)

    substractionResult = substraction(firstNumber, secondNumber)
    print("Substraction is: ", substractionResult)

    multiplicationResult = multiplication(firstNumber, secondNumber)
    print("Multiplication is: ", multiplicationResult)

    divisionResult = division(firstNumber, secondNumber)
    print("Division is: ", divisionResult)

if __name__ == "__main__":
    main()
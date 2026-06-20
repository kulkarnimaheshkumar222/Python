from Module import *

def main():
    firstNumber = int(input("Enter first number"))
    secondNumber = int(input("Enter second number"))

    result = addition(firstNumber, secondNumber) 
    print("Addition is: ", result)
    
    result = substraction(firstNumber, secondNumber)
    print("Substraction is: ", result)

if __name__ == "__main__":
    main()

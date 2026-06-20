import Module

def main():
    firstNumber = int(input("Enter first number"))
    secondNumber = int(input("Enter second number"))

    result = Module.addition(firstNumber, secondNumber) 
    print("Addition is: ", result)

if __name__ == "__main__":
    main()

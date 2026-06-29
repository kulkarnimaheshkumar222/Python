# 2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
# Input: 10 20
# Output: 20 is greater

def ChkGreater(firstNumber, secondNumber):
    if firstNumber > secondNumber:
        return firstNumber
    elif firstNumber == secondNumber:
        return None
    else:
        return secondNumber

def main():
    firstNumber = int(input("Enter first number"))
    secondNumber = int(input("Enter second number"))
    result = ChkGreater(firstNumber,secondNumber)
    if result is None:
        print("Both numbers are equal")
    else:
        print(result, "is greater")

if __name__ == "__main__":
    main()


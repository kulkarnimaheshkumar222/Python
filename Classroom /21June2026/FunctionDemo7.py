def calculation(number1,number2):
    multiplicationResult = number1 * number2
    divisionResult = number1 / number2
    return multiplicationResult, divisionResult

def main():
    multiplicationResult, divisionResult = calculation(20,10)

    print("Multiplication is : ", multiplicationResult)
    print("Division is : ", divisionResult)

if __name__ == "__main__":
    main()
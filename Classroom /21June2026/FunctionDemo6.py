def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 // number2

def main():
    multiplicationResult = multiplication(10,20)
    print("Multiplication is : ", multiplicationResult)

    divisionResult = division(200,10)
    print("Division is: ", divisionResult)


if __name__ == "__main__":
    main()
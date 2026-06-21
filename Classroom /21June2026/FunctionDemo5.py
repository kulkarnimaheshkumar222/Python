# Accept: Multiple Parameter
# Return: Multiple Values

def marvellous(value1, value2):
    print("Inside marvellous function: ", value1, value2)
    return value1, value2

def main():
    result1, result2 = marvellous(11,21)
    print("Returned Values are : ", result1, result2)


if __name__ == "__main__":
    main()
# Accept: One Parameter
# Return: One Value

def marvellous(value):
    print("Inside marvellous function: ", value)
    return value + 10 

def main():
    result = marvellous(11)
    print("Returned Value: ", result)


if __name__ == "__main__":
    main()
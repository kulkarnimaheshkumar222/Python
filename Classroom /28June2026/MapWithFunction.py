def checkEven(number):
    return (number%2 == 0)

def incrementNumber(number):
    return number+1

def main():
    data = [13,12,8,10,11,20]
    print("Input data is: ", data)

    filteredData = list(filter(checkEven, data))
    print("Filtered data is: ", filteredData)

    mappedData = list(map(incrementNumber, filteredData))
    print("Mapped data is: ", mappedData)

if __name__ == "__main__":
    main()
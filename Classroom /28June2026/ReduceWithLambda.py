from functools import reduce

checkEven = lambda number: number%2 == 0

incrementNumber = lambda number: number + 1

addition = lambda number1, number2: number1 + number2

def main():
    data = [13,12,8,10,11,20]
    print("Input data is: ", data)

    filteredData = list(filter(checkEven, data))
    print("Filtered data is: ", filteredData)

    mappedData = list(map(incrementNumber, filteredData))
    print("Mapped data is: ", mappedData)

    reducedData = reduce(addition, mappedData)
    print("Reduced data is: ", reducedData)

if __name__ == "__main__":
    main()
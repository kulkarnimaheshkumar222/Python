from functools import reduce

checkEven = lambda number: number%2 == 0

incrementNumber = lambda number: number + 1

addition = lambda number1, number2: number1 + number2

def filterX(task, elements):
    result = list()

    for element in elements:
        value = task(element) # checkEven(element)
        if value:
            result.append(element)
    return result

def mapX(task,elements):
    result = list()

    for element in elements:
        value = task(element) # incrementNumber(element)
        result.append(value)
    return result

def reduceX(task, elements):
    result = 0

    for element in elements:
        result = task(result, element)
    return result

def main():
    data = [13,12,8,10,11,20]
    print("Input data is: ", data)
    
    filteredData = list(filterX(checkEven, data))
    print("Filtered data is: ", filteredData)

    mappedData = list(mapX(incrementNumber, filteredData))
    print("Mapped data is: ", mappedData)

    reducedData = reduceX(addition, mappedData)
    print("Reduced data is: ", reducedData)

if __name__ == "__main__":
    main()
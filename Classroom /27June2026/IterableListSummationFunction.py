def summation(array):
    sum = 0
    for item in array:
        sum = sum + item
    return sum

def main():
    marks = [78,90,56,98,77]
    result = summation(marks)
    print("Sum is: ", result)

if __name__ == "__main__":
    main()
def summation(array):
    sum = 0
    for item in array:
        sum = sum + item
    return sum

def main():
    size = 0
    arr = list()
    size = int(input("Enter no of elements"))

    print("Enter elements")

    for item in range(size):
        no = int(input())
        arr.append(no)

    result = summation(arr)

    print("Summation is: ", result)

if __name__ == "__main__":
    main()
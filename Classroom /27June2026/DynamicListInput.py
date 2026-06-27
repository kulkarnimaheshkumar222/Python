def main():
    size = 0
    arr = list()
    size = int(input("Enter no of elements"))

    print("Enter elements")

    for item in range(size):
        no = int(input())
        arr.append(no)

    print(arr)

if __name__ == "__main__":
    main()
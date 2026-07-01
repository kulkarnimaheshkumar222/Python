# 5. Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 5 4 3 2 1

def displayReverseNumbers(number):
    for item in range(number, 0, -1):
        print(item, end = " ")

def main():
    number = int(input("Enter number"))
    displayReverseNumbers(number)

if __name__ == "__main__":
    main()
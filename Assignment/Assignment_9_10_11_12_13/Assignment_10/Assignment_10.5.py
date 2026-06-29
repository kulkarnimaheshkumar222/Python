# 4. Write a program which accepts one number and prints all odd numbers till that number.
# Input: 10
# Output: 1 3 5 7 9

def displayOddNumbers(number):
    for i in range(1, number+1):
        if i%2 != 0:
            print(i, end=" ")

def main():
    number = int(input("Enter number"))
    displayOddNumbers(number)

if __name__ == "__main__":
    main()
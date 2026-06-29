# 2. Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5, Output: 15

def sumOfNumber(number):
    sum = 0
    for i in range(number+1):
        sum = sum + i
    return sum

def main():
    number = int(input("Enter number"))
    result = sumOfNumber(number)
    print("Sum is: ", result)

if __name__ == "__main__":
    main()
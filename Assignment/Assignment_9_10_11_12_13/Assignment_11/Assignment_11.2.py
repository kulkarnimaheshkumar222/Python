# 2. Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def countOfDigit(number):
    count = 0
    originalNumber = number
    while originalNumber > 0 :
        originalNumber = originalNumber/10
        count = count+1
    return count

def main():
    number = int(input("Enter number"))
    result = countOfDigit(number)
    print("Count of digit in number: ", number, "is:", result)

if __name__ == "__main__":
    main()
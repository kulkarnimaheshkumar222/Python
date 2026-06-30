# 3. Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

def sumOfDigit(number):
    sum = 0
    originalNumber = number
    while originalNumber > 0 :
        digit = originalNumber%10
        sum = sum + digit
        originalNumber = originalNumber//10
    return sum

def main():
    number = int(input("Enter number"))
    result = sumOfDigit(number)
    print("Sum of digit of number: ", number, "is:", result)

if __name__ == "__main__":
    main()
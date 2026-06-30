# 5. Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def isPalindromeNumber(number):
    originalNumber = number
    reverse = 0
    while originalNumber>0:
        digit = originalNumber%10
        reverse = reverse*10 + digit
        originalNumber = originalNumber//10
    return reverse == number

def main():
    number = int(input("Enter number"))
    result = isPalindromeNumber(number)
    print(number, "is palindrom number" if result else "is not palindrom number")

if __name__ == "__main__":
    main()
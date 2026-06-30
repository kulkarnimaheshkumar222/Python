# 4. Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def reverseNumber(number):
    reverse = 0
    originalNumber = abs(number)
    while originalNumber > 0 :
        digit = originalNumber%10
        reverse = reverse*10 + digit
        originalNumber = originalNumber//10
    return reverse

def main():
    number = int(input("Enter number"))
    result = reverseNumber(number)
    print("Reverse of : ", number, "is:", -result if number<0 else result)

if __name__ == "__main__":
    main()
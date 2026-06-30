# 1. Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

def isPrimeNumber(number):
    for i in range(2,number):
        if number%i == 0 :
            return False
    return True

def main():
    number = int(input("Enter number"))
    result = isPrimeNumber(number)
    print(number, "is prime number" if result else "is not primer number")

if __name__ == "__main__":
    main()
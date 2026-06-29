# 3. Write a program which accepts one number and prints factorial of that number.
# Input: 5, Output: 120

def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact = fact*i
    return fact

def main():
    number = int(input("Enter number"))
    if number < 0:
        print("Factorial of negative number is not possible")
        return 
    result = factorial(number)
    print("Factorial of", number, "is: ", result)

if __name__ == "__main__":
    main()
# 3. Write a program to accept one number and print square of that number.
# Input: 5 , Output: 25

def square(number):
    return number*number

def main():
    number = int(input("Enter number"))
    result = square(number)
    print("Square of ", number ,"is", result)

if __name__ == "__main__":
    main()
# 4. Write a program to accept one number and print cube of that number.
# Input: 5 , Output: 125

def cube(number):
    return number*number*number

def main():
    number = int(input("Enter number"))
    result = cube(number)
    print("Cube of ", number ,"is", result)

if __name__ == "__main__":
    main()
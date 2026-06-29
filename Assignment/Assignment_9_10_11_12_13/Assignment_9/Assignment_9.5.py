# 5. Write a program to accept one number and check whether it is divisible by 3 & 5
# Input: 15 , Output: Divisible by 3 & 5

def isDivisible(number):
    if number%3 == 0 and number%5 == 0:
        return True
    else:
        return False

def main():
    number = int(input("Enter number"))
    result = isDivisible(number)
    if result:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()

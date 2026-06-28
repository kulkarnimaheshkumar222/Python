def isEvenOdd(number):
    if number%2 == 0:
        return True
    else:
        return False
    
def main():
    value = int(input("Enter number"))
    result = isEvenOdd(value)
    print(value , "is even number" if result else "is odd number") 

if __name__ == "__main__":
    main()
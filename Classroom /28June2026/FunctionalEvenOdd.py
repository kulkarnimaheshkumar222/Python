isEvenOdd = lambda number: number%2 == 0

def main():
    value = int(input("Enter number"))
    result = isEvenOdd(value) # result = (value%2 == 0)
    print(value , "is even number" if result else "is odd number") 

if __name__ == "__main__":
    main()
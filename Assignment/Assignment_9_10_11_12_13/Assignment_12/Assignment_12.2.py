# 2. Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1 2 3 4 6 12

def displayFactors(number):
    result = list()
    for i in range(1, number+1):
        if number%i == 0:
            result.append(i)
    return result
    
def main():
    number = int(input("Enter number"))
    result = displayFactors(number)
    for item in result:
        print(item, end = " ")

if __name__ == "__main__":
    main()
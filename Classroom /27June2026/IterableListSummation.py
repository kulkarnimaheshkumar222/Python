def main():
    marks = [78,90,56,98,77]
    sum = 0
    for mark in marks:
        print(mark)
    marks[2] = 59
    print("-"*15)
    for mark in marks:
        print(mark)
    print("Sum is: ", sum)

if __name__ == "__main__":
    main()
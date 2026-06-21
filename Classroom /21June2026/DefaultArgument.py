def areaOfCircle(radius, PI = 3.14):
    return PI * radius * radius

def main():
    area = areaOfCircle(10)
    print("Area of circle is: ", area)

if __name__ == "__main__":
    main()
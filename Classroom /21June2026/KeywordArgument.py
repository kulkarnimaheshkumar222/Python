def areaOfCircle(radius, PI):
    return PI * radius * radius

def main():
    area = areaOfCircle(PI = 3.14, radius = 10)
    print("Area of circle is: ", area)

if __name__ == "__main__":
    main()
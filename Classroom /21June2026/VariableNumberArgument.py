def display(*data):
    print(data)
    print(type(data))

def main():
    display(10,"20",30.6,True,50)
   
if __name__ == "__main__":
    main()
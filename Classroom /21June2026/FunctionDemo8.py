def bigBazar():
    print("Inside bigBazar")

    def amul():
        print("Inside amul ice cream parlor")

    amul()

def main():
    bigBazar()
    amul() # Error
    bigBazar.amul() # Error

if __name__ == "__main__":
    main()
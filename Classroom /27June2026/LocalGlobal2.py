no = 11 # Global Variable

def display():
    a = 21 # Local Variable
    print("From display: ", no)
    print("From display value of a is : ", a)

def demo():
   # print("From demo value of a is: ", a) Error, because a is local variable of display function
    print("From demo: ", no)

display()
demo()
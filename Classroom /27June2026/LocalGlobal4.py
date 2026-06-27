no = 11 

def display():
    global no
    no = 21
    print("From display: ", no)
   
print("Before: ", no)
display()
print("After: ", no)

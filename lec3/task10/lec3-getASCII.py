while True:
    x=input("enter a char : ")
    if len(x) != 1 :
        print("enter a valid char")
    else :
        print("ASCII : "+str(ord(x)))
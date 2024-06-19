import mymodule
mylist=["www.google.com","www.youtube.com","www.facebook.com","www.linkedin.com"]
length=str(len(mylist))
print(mylist)
x=input("choose a website [1 - "+length+"] : ")
print("")
mymodule.firefox(mylist[int(x)-1])

body="#include <iostream>\n\nint main(){ \nreturn 0;\n}\n"
Name=input("ENter your name : ")
Role=input("ENter your role : ")
Dep=input("ENter your department : ")
head="#"*30 + f"#\n\n CopyRight for {Name}\n\n" + "#"*30 + f"\n#Role : {Role}\n\
#Department : {Dep}\n"
print(head)
f=open("out.cpp", 'w')
f.write(head+body)
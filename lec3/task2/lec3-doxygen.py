#parses header files and shows functions with their return type and arguments
import csv
f=open("DIO.h", 'r')
o=open("out.csv", 'w')
lines = f.readlines()
csvreader=csv.writer(o)
csvreader.writerow(["name", "type", "args", "ID"])
#print(lines)
id=0
for i in lines:
    if i == "\n" or "//" in i:
        continue
    #print(i)
    if "(" in i:
        splitted=i.split()
        print("type : "+splitted[0])
        if splitted[0] in ["void", "int", "float", "bool", "char","uint8_t","uint16_t","uint32_t"]:
            rem=" ".join(splitted[1:])
            #print(rem)
            name=rem.split("(")[0]
            print("name : "+rem.split("(")[0])
            args=("".join(rem.split("(")[1])).split(")")
            print(args[:-1])
            csvreader.writerow([name, splitted[0], str(args[:-1]),"IDx"+str(id)])
            id+=1
            print()
f.close()
o.close()
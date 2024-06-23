#creates a function that sets I/O directions for specific port of a uController
dir=[]
for i in range(0,8):
    dir.append("0" if input(f"enter pin {i} mode : ") == "in" else "1")
print(dir)
f=open("port.cpp",'w')
f.write("void GPIO_MODE(){\n\tGPIO_PORTF_DIR_R=0x"+"".join(dir)+";\n}")
f.close()
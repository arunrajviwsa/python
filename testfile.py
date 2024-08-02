"""f_sample =open("sample.txt")
read_content =f_sample.read();
print(read_content)
f_sample.close()"""
#f_demo =open("sample.txt","w")
f_demo = open("sample.txt","a")
f_demo.write("data\n")
f_demo.write("transfer\n")
f_demo.write("done\n")
f_demo.write("*"*70)
f_demo.close();
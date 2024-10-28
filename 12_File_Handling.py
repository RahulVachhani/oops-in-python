

# For Read only
f = open('12_file.txt','r')        # 'r' is default mode for file handling 

# print(f.read())  # its read all the lines
# print(f.readline()) # its read first line

# print(f.readlines()) # its read all the lines 
f.close()


# For Write In The FIle
f1 = open('12_file1.txt','w')   # if file in not exist then it create new one

f1.write('''new one added
city gandhinagar
college LDRP
''')
f1.close()

# for append the data to existing file
f2 = open('12_file1.txt','a')
f2.write("Hello")
f2.close()


# for copy one file to another 
f3 = open('12_file.txt','r')  # for copy image , use 'rb'<-- Read Binary

f4 = open('12_file3.txt','w')

for i in f3:
    f4.write(i)

f3.close()



# in given file handlingn automaticaly file close operation are perform we can write menualy
with open('12_file4.txt','w') as f:
    f.write('hello')

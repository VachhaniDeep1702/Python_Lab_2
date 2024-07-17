file1 = open("deep.txt", 'w')
file1.write("this is for assignment" )

file1.close()

file1 = open("deep.txt", 'r')
read = file1.read()
print(read)

file1.close()
import filecmp

file1 = open("file1.txt","w+")
file2 = open("file2.txt","w+")

for i in range(10):
     file1.write("This is line %d\r\n" % (i+1))

for i in range(10):
     file2.write("This is line %d\r\n" % (i+1))
file1.flush()
file2.flush()
print(filecmp.cmp('file1.txt','file2.txt'))

file1.write("newstuff")
file1.flush()
print(filecmp.cmp('file1.txt','file2.txt'))
file1.close()
file2.close()
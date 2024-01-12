fileref = open("text.txt","r")  #file openning with r = reading mode.
line = fileref.read()           #storing file content.
print(line[:100])               #printing stored content
fileref.close()                 #closing file

# fileread2 = open("/suu/Desktop/testfile.txt")
# line2 = fileread2.read()
# print("\n", line2)
# fileread2.close()
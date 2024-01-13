file_obj = open("square.txt", "w")
for num in range(13):
    square = num*num
    file_obj.write(str(square) + "\n")
file_obj.close()

new_file_obj = open("square.txt","r")
print(new_file_obj.read())
new_file_obj.close()
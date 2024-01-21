li = []
print('empty list:')
print(li)
print('\n')

li1 = [1,2,3,4,5]
print('num list:')
print(li1)
print('\n')

li2 = [1,"apple",3,"num",5,"chars"]
print('mix list:')
print(li2)
print("single item from list => "+li2[1])           #printing single item from list.
print("single item from list => "+li2[-1])           #printing single item from list using negative indexing.
print('\n')

liSlice = ['p', 'r', 'o', 'g', 'a', 'm', 'i', 'n', 'g']
print(liSlice)

#slicing of list
print("\nSlicing of li:")
print(li2[2:5])
print(li2[:-3])
print(li2[3:])
print(li1[3:])

#new list
print("\n new list:")
li3 = [1,2,3,4,56,6,7,8,9,0,10]
print(li3)

#changing list element
print("\nchanging list element:")
li3[3] = 33
print(li3)

print("\nchanging multiple elements in list:")
li3[3:6] = [1,2,3]
print(li3)

#Operation on list
print("\nOpperation on list:")
li4 = li1 + li2
print("list4: ",li4)
print(li4*3)

print("\ndeleting item from the list:")
del li4[3]
print(li4)
print(li4.pop())

print("Taking input from the user:")
li6 = []
for i in range(10):
    num = int(input("Enter li item: "))
    li6.append(num)
    
print("\n")
print(li6)

pow1 = []
for x in range(10):
    pow1.append(2**x)
    
print("\nPower list: ",pow1)

print("\nPrinting list item by item: ")
for i in pow1:
    print(i)
  
[x+y for x in ["py", "c"] for y in ["lang", "prog"]]
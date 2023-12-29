import math
n = int(input("\nEnter num: "))

if(n <= 0):
    print("Invalid input!")
else:
    c = n % 2
    if(c == 0):
        print("Root of ",n," is",math.sqrt(n),"\n")
    else:
        print("Square of ",n," is",n*n,"\n")
    
p = int(input("Enter Percentage: "))
if(p >= 0 and p <= 100):
    if(p >= 90):
        print("Grade A\n")
    
    elif(p >= 75 and p < 90):
        print("Grade B\n")
    
    elif(p >= 60 and p < 75):
        print("Grade C\n")
    else:
        print("Grade D\n")
        
else: 
         print("Invalid percentage Entered!!\n")
    

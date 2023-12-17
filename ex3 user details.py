user_no = int(input("\nEnter the Number of user:\n "))      #Taking no of users
d={}
for i in range(0, user_no):                                 #Taking user input data with loop
    uid = int(input("\nEnter User's ID: \n"))
    u_name = input("Enter User's Name:\n ")
    age = int(input("Enter User's Age: \n"))
    d[uid]=[u_name,age]                                     #Inserting data to dict.
   
su=int(input("\nEnter the UID of the particular user: \n"))
print(d[su],"\n")
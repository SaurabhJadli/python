n = int(input("\nEnter num: "))

if(n <= 0):
    print("Invalid input!")
else:
    c = n % 2
    if(c == 0):
        print("Entered no. was Even.\n")
    else:
        print("Entered no. was Odd.\n")
    
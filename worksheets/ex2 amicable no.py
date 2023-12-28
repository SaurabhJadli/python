#Write a function to print pairs of amicable numbers in a range.

def proper_divisors_sum(num):
    divisors_sum = 1 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:  
                divisors_sum += num // i
    return divisors_sum

def find_amicable_numbers_in_range(start, end):
    amicable_pairs = []                 #Creating empty array for storing amicable nno.
    for num in range(start, end + 1):
        potential_amicable = proper_divisors_sum(num)
        if (
            num != potential_amicable
            and proper_divisors_sum(potential_amicable) == num
            and num < potential_amicable  #To avoid duplicates and ensure each pair is only listed once
        ):
            amicable_pairs.append((num, potential_amicable))
    return amicable_pairs

start_range = int(input("\nEnter starting range: "))        #Taking user input
end_range = int(input("Enter ending range: "))

amicable_pairs = find_amicable_numbers_in_range(start_range, end_range)

if amicable_pairs:
    print("\nAmicable no. pairs in range", start_range, "to", end_range, ":")
    for pair in amicable_pairs:
        print(pair[0], "-", pair[1])
else:
    print("\nNo amicable number pairs found in the range", start_range, "to", end_range)

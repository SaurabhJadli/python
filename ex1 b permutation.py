#     b) Write a program to implement these formulae of permutations and combinations. 
# Number of permutations of n objects taken r at a time: p(n, r) = n! / (n-r)!.
# Number of combinations of n objects taken r at a time is: c(n, r) = n! / (r!*(n-r)!) = p(n,r) / r!

def f(a):
    fact = 1
    for i in range(1, a+1):
        fact = fact*i
    return fact


def perCo(n, r):
    x = n - r
    p = f(n)/f(x)
    print("\nPermutaton:", p)
    c = f(n)/f(x)*f(r)
    print("\nCombination:", c, "\n")

perCo(3, 2)
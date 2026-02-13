# 4. WA recursive function to calculate the sum of first n natural numbers.
def sum_of_natural_numbers(n):
    if(n<=0):
        return 0
    else:
        return n+ sum_of_natural_numbers(n-1)
    
n = int(input("Enter a positive integer: "))
sum_natural =  sum_of_natural_numbers(n)
print(f"The sum of first {n} natural numbers is: {sum_natural}")
# Take P , N and R as input from user
P = float(input('please enter principle in INR : '))
N = float(input('please enter Period in Year : '))
R = float(input('please enter rate of Intrest in %p.a : '))
A = P*(1+R/100)**N
I = A - P
# Print above results
print(f'Amount for Compound intrest : {A:.2f} INR')
print (f'Total Intrest : {I:.2F} INR')

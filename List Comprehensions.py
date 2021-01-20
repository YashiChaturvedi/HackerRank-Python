#Input
x = int(input())
y = int(input())
z = int(input())
n = int(input())

#Solve
my_list = [[P, Q, R] for P in range(x+1) for Q in range(y+1) for R in range(z+1) if P + Q + R != n]

#Output
print(my_list)
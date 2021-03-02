# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ab = []

ab.append(a)
ab.append(b)

prod = list(product(*ab))

print(*prod, sep=" ")

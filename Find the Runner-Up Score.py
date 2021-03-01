n = int(input())
mylist = list(map(int, input().split()))

newlist = set(mylist)

newlist.remove(max(newlist))

print(max(newlist))
n = int(input())
d = {}

for i in range(n):
    data = input().split(' ')
    d[data[0]] = data[1]

while (True):
    try:
        a = input()

        if a in d.keys():
            print(a + "=" + d[a])
        else:
            print("Not found")
    except:
        break
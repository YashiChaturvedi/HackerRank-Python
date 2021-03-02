def execute(lst, cmd, *args):
    if cmd == 'insert':
        lst.insert(int(args[0]), int(args[1]))
    elif cmd == 'print':
        print(lst)
    elif cmd == 'remove':
        lst.remove(int(args[0]))
    elif cmd == 'append':
        lst.append(int(args[0]))
    elif cmd == 'sort':
        lst.sort()
    elif cmd == 'reverse':
        lst.reverse()
    elif cmd == 'pop':
        lst.pop()
    else: 
        print("Command not recognized!")

lst = []
for _ in range(int(input())):
    execute(lst, *input().split())

n = int(input().strip())
examine = {True: "Not Weird", False: "Weird"}

print(examine[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])

n = 5

for i in range(n, 0, -1):
    for j in range(1, i):
        if i==n or j==1 or j==i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

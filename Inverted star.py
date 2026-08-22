n = 5

for i in range(n , 0 , -1):

    for j in range(1, i):

        if j == 1 or j == i-1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
    

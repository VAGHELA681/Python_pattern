n = 10
#outer loop
for i in range(1, n):
    #spaces ( n - i )
    for j in range(1, n - i):
        print(" ", end=" ")
    #inner loop
    for k in range(1, i):
        print("*", end=" ")
    
    print()
    

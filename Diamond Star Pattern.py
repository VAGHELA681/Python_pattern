#upper half
for i in range(1, 6):

    # spaces
    for j in range(5 - i):
        print(" ", end="")

    # stars
    for k in range(1 ,i):
        print(" *", end="")

    print()
 
#lower half
for i in range(4 , 0 , -1):

    # spaces
    for j in range(5 - i):
        print(" ", end="")

    # stars
    for k in range(1 ,i):
        print(" *", end="")

    print()

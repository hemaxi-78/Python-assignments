for row in range(1,6):
    for colum in range(0,row):
        if row%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()
for row in range(1,6):
    for colum in range(1,6):
        if row==3 and colum==3:
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()
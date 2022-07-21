positive_list=[]
negetive_list=[]
for i in range(1,6):
    num=int(input("enter number:="))
    if num>0:
        positive_list.append(num)
    else:
        negetive_list.append(num)
print(positive_list)
print(negetive_list)
list=[]
n=int(input("enter number of elements:"))
for i in range(n):
    list.append(int(input()))
list=lst(set(list))
list.sort()

print("sorted list-",list)
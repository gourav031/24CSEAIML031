i=input("enter a sentence-:")
LIST1=i.split()
print("\n Elements of LIST1 with index-:")
for i,w in enumerate (LIST1):
    print(i,w)
LIST2=list(range,len([LIST1])+1)
LIST3=list(zip(LIST1,LIST2))
print("\ncombined LIST3 using zip-:")
print(LIST3)
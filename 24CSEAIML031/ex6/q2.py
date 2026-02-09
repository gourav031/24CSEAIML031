d={}
n=int(input("enter number of key value pairs-:"))
for i in range (n):
    k=input("enter key-:")
    v=input("enter value-:")
    d[k]=v
rev={}
for k,v in d.items():
    rev[v]=k
print("\noriginal dictionary-:")
print(d)
print("\nreversed dictionary(values as keys)-:")
print(rev)
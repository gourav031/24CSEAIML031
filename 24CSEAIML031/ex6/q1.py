l=["banana","orange","apple"]
print("list of fruits are displayed from last index to first index")
for i in l[::-1]:
    print(i,"lenghth:",len(i))
rev=[]
for s in l:
    rev.append(s[::-1])
print(rev)


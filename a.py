a=["Mango","Apple","Grapes","Pineapple","Mango","Apple"]
b=set(a)
print(b)
b=[]
for i in a:
    if(a.count(i)>1 and (i not in b)):
        b.append(i)
print(b)


    

import itertools
l,t=[2,5,2,1,2],5
result=[]
for w in range(2,len(l)):
    for each in list(itertools.combinations(l,w)):
        s=0
        for x in each:
            s+=x
        if s==t:
            result.append(list(each))


for ls in l:
    if ls==t:
        result.append(ls)

list(set(result))
rs=result.copy()

for i,v in enumerate(rs):
    rs=result.copy()
    sr.append(set(rs.pop(i)))

print(sr)

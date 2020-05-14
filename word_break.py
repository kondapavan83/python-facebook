wordDict=['apple', 'pen', 'applepen', 'pine', 'pineapple']
s='pineapplepenapple'
str=(s,)

for each in wordDict:
    while 1:
        for every in str:
            if each in every:
                str=every.rpartition(each)
        c=0
        for every1 in str:
            if each not in every1:
                c+=0
            else:
                c+=1
        print(str)
        if c==1:
            continue
        else:
            break
-------------------------------------------------------------------
sp=[]
sd={}
for word in wordDict:
     for each in str:
             sp.append(list(each.rpartition(word)))

for i in sp:
     for j,k in enumerate(i):
             if k!='':
                     i[j]=k.rsplit(word)
             else:
                     i.pop(j)
sd={}
for word in wordDict:
    sd[word]=s.split(word)

for word,lis in sd.items():
    w=wordDict.copy()
    w.remove(word)
    for wrd in w:
            for each in lis:
                    if each=='':
                            continue
                    else:
                            x=each.split(wrd)
                            sd[word].append({wrd:(x)})


-------------------------------------------------
dc={}
for word in wordDict:
     dc[word]=[]


for word in wordDict:
     if word in st:
             indx=st.index(word)
             dc[word].append(indx)
             for i in range(int(len(st)/2)+1):
               if indx <= len(st) and word in st[indx+len(word):]:
                        indx1=indx
                        indx2=st[indx+len(word):].index(word)
                        indx=indx2+indx1+len(word)
                        dc[word].append(indx)
               else:
                        break
            

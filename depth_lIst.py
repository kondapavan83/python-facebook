def depth(ls):
    dptd={}
    dls=[]
    def extpop(ls,dpt=1):
         for i,v in enumerate(ls):
                 if type(v)==list:
                         dpt+=1
                         for p in v:
                             print(f"p={p}")
                             if type(p) != list:
                                 if dpt in dptd.keys():
                                     dptd[dpt].append(p)
                                 else:
                                     dptd[dpt]=[p]
                         temp=ls.pop(i)
                         print(f"temp={temp}")
                         ls.extend(temp)
                         print(f"ls={ls}")
                         extpop(temp,dpt)
                 else:
                     if dpt in dptd.keys():
                         dptd[dpt].append(v)
                         dpt=1
                         print(f"outv={v}")
                     else:
                         dptd[dpt]=[v]
    extpop(ls)
    return dptd


k=[[1,1],2,[1,1]]
depth(k)

import itertools
# l,t=[10,1,2,7,6,1,5],8
l,t=[2,5,2,1,2],5
# def csum(l,t):
result=[]
for i,j in enumerate(l):
    p=l.copy()
    pc=p.pop(i)
    pp=[]
    for k in range(len(l)-1):
       if pc+p[k] == t:
               if {pc,p[k]} in result:
                       continue
               else:
                       result.append({pc,p[k]})
    for w in range(2,len(l)-1):
        for each in list(itertools.combinations(p,w)):
            s=0
            for x in each:
                s+=x
            if pc+s==t:
                hold1=list(each)
                hold2=hold1.extend([pc])
                hold2
                if set(hold2) in result:
                    continue
                else:
                    result.append(set(hold2))




# csum([10,1,2,7,6,1,5],8)

# for i,j in enumerate(l):
#      p=l.copy()
#      p.pop(i)
#      pc=0
#      pp=[]
#      result=[]
#      for i in range(len(l)-1):
#              pc+=p(i)
#              pp.append(i)
#              if pc == 8:
#                      result.append(pp)

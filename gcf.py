#############################
#median of a list
#############################
l=[2, 3, 10, 20, 30, 56, 99]
p=l.copy()
d={}
for i in range(len(p)):
  k=p.pop()
  if k in d.keys():
    d[k]+=1
  else:
    d[k]=1

#############################
#GCF of all numbers in a list
#############################
def is_prime(x):
  for i in range(2,(int(x/2)+1)):
    if x%i==0:
      return False
      break
    else:
      continue
  return True
dct={}
gcf=[]
for i in p:
  dct[i]=[]
  for j in range(1,i):
    if i%j==0 and is_prime(j):
        dct[i].append(j)
        gcf.append(j)
    else:
        continue
gcf_unique=[]
for i in gcf:
    if i not in gcf_unique and gcf.count(i) == len(p):
        gcf_unique.append(i)

print(max(gcf_unique))

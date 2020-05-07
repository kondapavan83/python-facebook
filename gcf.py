#############################
#median of a list
#############################
l=[2, 3, 10, 20, 30, 65,23, 99,23,67,34,11]
#l=[696, 101, 509, 404, 484, 205, 258, 733, 930, 576, 923, 382, 475, 576, 806, 569, 221, 918, 770, 239, 747, 720, 393, 817, 744, 914, 767, 990, 16, 205, 741, 921, 530, 594, 927, 295, 564, 212, 137, 328, 18, 541, 413, 459, 416, 143, 31, 618, 169, 916]
# l=[696, 101, 509, 404, 484, 205, 258, 733, 930, 576, 923, 382, 475, 576, 806, 569, 221, 918, 770, 239, 747, 720, 393, 817, 744, 914, 767, 990, 16, 205, 741, 921, 530, 594, 927, 295, 564, 212, 137, 328, 18, 541, 413, 459, 416, 143, 31, 618, 169, 916, 1, 99, 20, 65, 49, 50, 78, 78, 27, 8, 38, 67, 31, 60, 78, 92, 28, 78, 41, 20]
p=l.copy()


################################
# GCF of all numbers in a list #
################################
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
  for j in range(2,i):
    if i%j==0 and is_prime(j):
        dct[i].append(j)
        gcf.append(j)
    else:
        continue
# print(f"\nlength of p is{len(p)}\n")
# print(f"\ngcf is {gcf} \n \n dct is {dct}")
gcf_unique=[]

for i in gcf:
    print(f"gcf count is {gcf.count(i)} and i is {i}")
    # if gcf.count(i) == len(p):
    #     gcf_unique.append(i)
    #     print(i)

print(f"\ngcf_unique is {gcf_unique}")

#gcf_value=max(gcf_unique)
#print(gcf_value)


print(f"\nlength of dict is {len(dct)}")
###################################
# most recurring number in a list #
###################################
p_uq={}
for i in p:
    p_uq[i]=p.count(i)

for k,v in p_uq.items():
    if v==max(list(p_uq.values())):
        print(f"most recurring number is {k}")

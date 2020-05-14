def flip(ip,k):
     nip=[]
     for i in range(len(ip[:k])-1,-1,-1):
             nip.append(ip[i])
     nip.extend(ip[k:])
     return nip

def produce_sequence(ip,sip):
    dct={}
    for i in range(10):
         k=random.choice(range(2,len(ip)+1))
         ip=flip(ip,k)
         #print(ip,k)
         dct[k]=ip
         if ip==sip:
                 break
    if sip in list(dct.values()):
        return dct
    else:
        produce_sequence()


def pancake_sort(ip):
    sip=sorted(ip)
    if sip==ip:
        return []
    else:
        return(produce_sequence(ip,sip))
pancake_sort([3,2,4,1])
#pancake_sort([1,2,3])

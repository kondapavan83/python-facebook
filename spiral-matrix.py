# r,c,rp,cp,l=1,4,0,0,[]
# r,c,rp,cp,l=5,6,1,4,[]
def spiral_matrix(r,c,rp,cp):
    ccp,crp=cp,rp
    l,mtrx=[],[[crp,ccp]]
    for i in range(c*r*2):
        for j in range(1,(c*r)):
            if j%2!=0:
                if cp<c*2:
                    cp+=j
                    l.append([rp,cp])
                if rp<r*2:
                    rp+=j
                    l.append([rp,cp])
            else:
                if cp<c*2:
                    cp-=j
                    l.append([rp,cp])
                if rp<r*2:
                    rp-=j
                    l.append([rp,cp])
    for i,v in enumerate(l):
        if v[0]==l[i+1][0] and v[1]==l[i+1][1] and -1<v[1]<c and r>v[0]>-1:
            mtrx.append(v)
        elif v[0]>l[i+1][0] and v[1]==l[i+1][1] and -1<v[1]<c:
            for i in range (v[0],l[i+1][0],-1):
                if r>i>-1:
                    mtrx.append([i,v[1]])
        elif v[0]<l[i+1][0] and v[1]==l[i+1][1] and -1<v[1]<c:
            for i in range (v[0],l[i+1][0]):
                if r>i>-1:
                    mtrx.append([i,v[1]])
        elif v[1]>l[i+1][1] and v[0]==l[i+1][0] and r>v[0]>-1:
            for i in range (v[1],l[i+1][1],-1):
                if -1<i<c:
                    mtrx.append([v[0],i])
        elif v[1]<l[i+1][1] and v[0]==l[i+1][0] and r>v[0]>-1:
            for i in range (v[1],l[i+1][1]):
                if -1<i<c:
                    mtrx.append([v[0],i])
    print(mtrx)

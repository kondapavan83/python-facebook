def trl_F(x):
    c,a=1,0
    for i in range(1,x+1):
        c*=i
    cs=str(c)
    for i in cs[::-1]:
        if i=='0':
          a+=1
    return a

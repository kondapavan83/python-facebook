def cdepth(ls,depth=1):
  depth=1
  dtls={}
  dtls[1]=[]
  lbit=1
  for i in ls:
    if type(i)==list:
      depth+=1
      lbit=1
      if depth in dtls.keys():
        dtls[depth].append(i)
      else:
        dtls[depth]=[i]
    elif type(i)!=list:
      dtls[1].append(i)
      lbit=0
  temp_dtls={}
  for k,v in dtls.items():
    if type(v)==list:
        for j in v:
          if type(j)==list:
            print(f"j={j}")
            cdepth(j,depth=k+1)
          else:
            if k+1 in temp_dtls.keys():
                temp_dtls[k+1].append(j)
            else:
                temp_dtls[k+1]=[j]
  return dtls,temp_dtls

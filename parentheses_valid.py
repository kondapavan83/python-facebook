def par(x):
  xl=[]
  spltindx=[]
  for i,v in enumerate(x):
      if x[i]==')' and x[i+1]=='(':
          spltindx.append(i)
  return spltindx
          xl.append(x[:i+1])
          xl.append(x[i+1:])
          print(i)
  print(xl)
  def par_cnt(k):
      c=0
      df=0
      for i in k:
        if i=='(':
          c+=1
        elif i==')':
          df+=1
      if c>df:
        r=c-df
      elif c<df:
        r=df-c
      else:
        r=0
      return r
  t=0
  for k in xl:
      t+=par_cnt(k)
  return t
for i in par(b):
     xl.append(b[:i+1])
     xl.append(b[i+1:])
     for j in len(1,par(b)):
             xl.extend(xl[-1][:(len(b)-par(b)[0])+1])

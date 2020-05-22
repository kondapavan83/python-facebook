#LEETcode Link: https://leetcode.com/problems/interval-list-intersections/
A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]

def expnd(A):
  Ali=[]
  for each in A:
     ali=[]
     for i in range(each[0],each[1]+1):
             ali.append(i)
     Ali.append(ali)
  return Ali

Ali=expnd(A)
Bli=expnd(B)

def set_intrsc(Ali,Bli):
  fr=[]
  for each in Ali:
     for beach in Bli:
             temp=list(set(each).intersection(set(beach)))
             if len(temp) ==0:
                 continue
             elif len(temp) ==1:
                 fr.append([temp[0],temp[0]])
             elif len(temp) ==2:
                 fr.append(temp)
             elif len(temp)>2:
                 fr.append([temp[0],temp[-1]])
  return fr

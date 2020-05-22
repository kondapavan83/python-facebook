#Leetcode link: https://leetcode.com/problems/custom-sort-string/
def custom_sort(S,T):
  l=[]
  pc=''
  for alpha in S:
      if alpha in T:
          pc+=alpha
  for letter in T:
       if letter in S:
               T=T.replace(letter,'')
               l.append(letter)
  return pc+T

S='back'
T='abcd'
custom_sort(S,T)

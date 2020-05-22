#Leetcode link: https://leetcode.com/problems/k-closest-points-to-origin/
def k_close_origin(k,points):
    ed={}
    answer=[]
    for p in points:
        ed[math.sqrt((p[0]**2)+(p[1]**2))]=p
    for i,v in enumerate(sorted(ed)):
        if i<k:
            answer.append(ed[v])
    return answer

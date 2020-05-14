def if_mountain(ls):
    pch=0
    for i in range(len(ls)):
        if sorted(ls[:i+1]) == ls[:i+1] and sorted(ls[i+1:],reverse=True)==ls[i+1:]:
            pch=i
    if pch==0:
        return False
    else:
        return pch        

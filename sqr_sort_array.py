def sq(ls):
    sq_ls=[]
    for each in ls:
        sq_ls.append(each**2)
    return(sorted(sq_ls))

ls=[-4,-1,0,3,10]
print(sq(ls))

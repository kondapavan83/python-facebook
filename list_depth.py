def lstdepth(ls):
    ld=[]
    ldic={}
    def lsdepth(ls,depth=1):
        for each in ls:
            if type(each)==list:
                depth+=1
                lsdepth(each,depth)
            else:
                ld.append(depth)
                ldic[each]=depth
        return(ldic)
    return(lsdepth(ls))
lstdepth([1,[2,3,[4,5,[6,7,[9,8,[10]]]]]])

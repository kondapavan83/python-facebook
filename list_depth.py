ldic={}
def depth(ls):
    depth=1
    for each in ls:
        if deep(each)>1:
            for every in each:
                ls.append()
    def deep():
        for elem in ls:
          if type(elem)==list:
            depth+=1
            return depth


flat_list = []
for sublist in nl:
    if type(sublist)==list:
        for item in sublist:
            flat_list.append(item)
            

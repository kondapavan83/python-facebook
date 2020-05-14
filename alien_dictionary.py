class alien_dic:
    def __init__(self,ls,order):
        ls=self.ls
        order=self.order
    def aliendictionary(ls,order):
        words=[]
        order_dict=dict(zip(order,range(26)))
        # for ind in range(len(ls)):
        #     if ind<=len(ls)-2:
        #         if len(ls[ind])>=len(ls[ind+1]):
        #             temp=True
        #         else:
        #             temp=False
        #
        # print("\ntemp = {}\n".format(temp))
        for word in ls:
            words.append(dict(zip(range(len(word)),word)))
        print(F"words={words} \n order_dict={order_dict}")
        for word in words:
            for k,v in word.items():
                if k+1<=len(v)-1 and order_dict[v[k+1]]>order_dict[v[k]]:
                    temp1=True
                else:
                    temp1=False


        print("\ntemp1 = {}\n".format(temp1))
        # if temp==True and temp1==True:
        if temp1==True:
            return True
        else:
            return False


print(alien_dic.aliendictionary(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))

def d2b(num):
    b=[]
    def DecimalToBinary(num):
        if num>1:
            DecimalToBinary(num // 2)
        b.append(num%2)
    DecimalToBinary(num)
    return(b)

def count_bits(x):
    onels=[]
    for num in range(x+1):
        ones=0
        bls=d2b(num)
        for bd in bls:
            #print(bd)
            if bd==1:
                ones+=1
        onels.append(ones)
    print(onels)

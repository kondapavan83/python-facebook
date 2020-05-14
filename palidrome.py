def ispalindrome(x):
    pc=None
    x=x.lower()
    a=''
    for i in x:
        if i.isalnum():
            a=a+i
    for i,j in enumerate(a):
        if a[i]==a[-(i+1)]:
            pc=True
            continue
        else:
            pc=False
            break
    return pc

print(ispalindrome(input()))

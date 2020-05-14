def prnth_valid(s):
    open=0
    close=0
    for character in s:
        if character =='(':
            open+=1
        elif character ==')':
            close+=1
        else:
            print("not a vlid string")
    diff=open-close
    if diff<0:
        diff_negative=True
        diff=diff*(-1)
    return(diff)

print(prnth_valid("())"))

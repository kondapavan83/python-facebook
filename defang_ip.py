def defang_ip(ip):
    dip=''
    dip=ip.split('.')
    # print(dip)
    dfip=''
    for oct in dip:
        if dfip=='':
            dfip=oct
        else:
            dfip=dfip+"[.]"+oct
    print(dfip)

defang_ip(input("Provide an ip address to defang:"))

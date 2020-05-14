def defang_ip(ip):
    dip=ip.split('.')
    dfip="[.]".join(dip)
    print(dfip)

defang_ip(input("Provide an ip address to defang:"))

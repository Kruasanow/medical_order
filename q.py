def sett(www):
    key='11100100'*len(www)
    deca=list(www)
    deca=[bin(ord(i))[-8::] for i in www]
    for i in range(len(deca)):
        if 'b' in deca[i]:
            deca[i]=deca[i].replace('b', '0')
    print(deca)
    q=''    
    xorres=''
    dec=''
    qqq=''
    for i in deca:
        q=q+i
    for i in range(len(key)):
        xorres=int(key[i])^int(q[i])
        qqq+=str(xorres)
    decc=[qqq[i:i+8] for i in range(0, len(qqq), 8)]
    for i in range(len(decc)):
        decc[i]=int(decc[i],2)
        decc[i]=chr(int(decc[i]))
        dec+=decc[i]
    return dec


www='1234567890-=йцукенгшщзхъфывапролджэячсмитьбю.'
dec=sett(www)
print(dec)
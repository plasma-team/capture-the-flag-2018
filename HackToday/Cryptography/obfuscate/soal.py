from decimal import *
from binascii import hexlify
from binascii import unhexlify

FLAG = #SIKRIT
###Format: HackToday{#SIKRIT}

def enkripik(m):
    m = float('0.'+str(int(str(hexlify(bytes(m, "utf-8")), "utf-8"),16)))
    enc,e,i,f,si,m1=1,1,0,1,1,0
    if m != 0:
        while enc != m1:
            m1 = enc
            e *= m*m
            i += 2
            f *= i*(i-1)
            si *= -1
            enc += e/f*si
        return str(hex(int(str(+enc)[2:])))[2:]
    return 1

m = [enkripik(FLAG[i:i+5]) for i in range(0, len(FLAG), 5)]

f=open("encrypted.txt", 'w')

for c in m:
    f.write("%s\n" % c)
f.close()

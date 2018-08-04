from PIL import Image
from binascii import *
def ck(ckc):
	ckck=0
	ckckc=1
	while(ckc):
		ckck=ckck+ckckc
		ckckc=ckck-ckckc
		ckc-=1
	return ckck
ckckck=1
flag=b"fakeflag"
ckckckc=hexlify(flag).decode('utf-8')
ckckckck = [ckckckc[ckckck:ckckck+2] for ckckck in range(0, len(ckckckc), 2)]
ckckckckc=[]
ckckck=1
while(len(ckckckck)!=0):
	if ck(ckckck)> len(ckckckck):
		ckckck=1
	else:
		ind=ck(ckckck)-1
		ckckckckc.append(ckckckck[ind])
		del ckckckck[ind]
		ckckck+=1
encoded = ''.join(ckckckckc)
ckckckckckckckck=['#'+encoded[ckckck:ckckck+6] for ckckck in range(0, len(encoded), 6)] 
j=0
for ckckck in ckckckckckckckck:
	im = Image.new("RGB", (100,100), ckckck)
	im.save( "color"+str(j)+".png")
	j+=1
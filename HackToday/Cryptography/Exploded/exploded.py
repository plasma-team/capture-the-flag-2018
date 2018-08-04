import random
import libnum
import math

flag = < Redacted >
nom = ""

for i in flag:
	nom += bin(ord(i))[2:].rjust(8, "0")

hehe = random.randint(1, 10)
for i in range(hehe):
	huhu = ""
	for j in range(len(nom)):
		huhu += nom[j]
		if(j % 2 == 0):
			huhu += nom[j] * i
		else:
			huhu += str(int(nom[j]) ^ 1) * i
	nom = huhu

enc = ""
for i in range(0, len(nom), 8):
	enc += chr(int(nom[i:i+8], 2))

open("flag.enc", "w").write(enc)

import random
import time

LEL = 7
LOL = range(LEL)
random.shuffle(LOL)

FLAG = open("flag.txt").read().strip()
LIL = FLAG

while len(LIL) % (2*LEL):
    LIL += "-"

for x in xrange(100):
    LIL = LIL[1:] + LIL[:1]
    LIL = LIL[0::2] + LIL[1::2]
    LIL = LIL[1:] + LIL[:1]
    temp = ""
    for y in xrange(0, len(LIL), LEL):
        for z in xrange(LEL):
            temp += LIL[y:y+LEL][LOL[z]]
    LIL = temp

def JK(flag):
	if(flag==FLAG):
		print "Your Flag is:",flag
	else:
		print "FALSE, Try again dude..."

print "Hai What's up ?..."
time.sleep(2)
print """
Send 1 to Get a string
Send 2 to Check the FLAG
"""
print "WELCOME TO EZ CRYPTO CHALLENGE"
idk = raw_input(">")
if idk=='1':
	print LIL
elif idk=='2':
	JK(raw_input(">"))
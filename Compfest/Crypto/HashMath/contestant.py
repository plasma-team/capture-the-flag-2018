MIN_LEN = 10**2
MAX_LEN = 10**3
MIN_WIN = 10
TIME_LIMIT = 100


import time
import random

flag = "CTFX{*}"

def hatching(str, mod):
	ret = 0
	for x in str:
		if 'a' > x or x > 'z':
			raise Exception('you must enter lower case letter, not {}'.x);
		ret = 26 * ret + ord(x) - ord('a')
		ret %= mod
	return ret


def hash_slinging_slicer(str1, str2, _len, mod):
	if len(str1) != _len or len(str2) != _len:
		raise Exception('length error')
	if str1 == str2:
		raise Exception('same string')
	if hatching(str1, mod) != hatching(str2, mod):
		raise Exception('the hash must be same')


startTime = int(time.time())
winNum = 0
while(winNum < MIN_WIN):
	N = random.randint(MIN_LEN, MAX_LEN)
	M = {**some random algorithm wkwkkwk**}
	print 'N = {}\tM = {}'.format(N, M)
	try:
		hash_slinging_slicer(raw_input(), raw_input(), N, M)
		winNum += 1
	except Exception as e:
		pass

if(winNum == MIN_WIN and int(time.time()) - startTime <= TIME_LIMIT):
	print flag

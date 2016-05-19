import sys
sys.setrecursionlimit(20000)

def shift(prime,numberlist):
	return list(filter(lambda x : x%prime != 0,numberlist))

def primeSieve(numberlist):
	if numberlist == []:
		return []
	else:
		prime = numberlist[0]
		return [prime] + primeSieve(shift(prime,numberlist[1:]))


print(primeSieve(list(range(2,10000))))



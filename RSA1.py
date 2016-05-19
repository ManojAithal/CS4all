import sys
import random
sys.setrecursionlimit(20000)

def shift(prime,numberlist):
	return list(filter(lambda x : x%prime != 0,numberlist))

def primeSieve(numberlist):
	if numberlist == []:
		return []
	else:
		prime = numberlist[0]
		return [prime] + primeSieve(shift(prime,numberlist[1:]))

def inverse(e,m):
	return [ d for d in range(1,m) if (e*d)%m ==1][0]
	

def makeEncoderDecoder():
	p,q = random.sample(primeSieve(range(2,50)),2)
	n=p*q
	m=(p-1)*(q-1)
	print("Maximum number that can be encrypted is ",n-1)	
	e =  random.choice(primeSieve(list(range(2,m))))
	if m%e == 0:
		print("Try again")
		return
	else:
		d = inverse(e,m)
		encoder = lambda x:(x**e)%n 
		decoder = lambda y:(y**d)%n
		return [encoder,decoder]

AliceEncrypt, AliceDecrypt = makeEncoderDecoder()

a=int(input("enter number to be encrypted:"))
print("Encrypted VAlue : ",AliceEncrypt(a))
print("Decrypted Value : ",AliceDecrypt(AliceEncrypt(a)))

import math
import random
import sys
from bisect import insort_left

#### Will move this to bottom of file later ####

file = open(sys.argv[1], 'r')

A = []

for line in file:
	A.append(int(line))

A.sort()
while len(A) > 1:
	# doesn't work
	#A.append(abs(A.pop() - A.pop()))
	insort_left(A, abs(A.pop() - A.pop()))

print A

def kk(A):
	A.sort()
	while len(A) > 1:
		insort_left(A, abs(A.pop() - A.pop()))
	return A

def genrandS(n):
	S = []
	for i in range(n):
		if random.random() < 0.5:
			S.append(1)
		else:
			S.append(-1)
	return S

#def neighS(S):


def genrandP(n):
	P = []
	for i in range(n):
		P.append(random.randrange(1, n))
	return P

def resP(S, A):
	X = [0] * len(A)
	for j in range(len(A)):
		X[S[j]] += A[j]

	return kk(X)


def neighP(S):
	N = S
	i = random.randrange(1, len(S))
	j = random.randrange(1, len(S))

	


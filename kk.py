import math
import random
import sys
import copy
from bisect import insort_left


max_iter = 25000

def kk(A):
	A.sort()
	while len(A) > 1:
		insort_left(A, abs(A.pop() - A.pop()))
	return A[0]

### Cooling Function ###
def T(iter):
	return math.pow(10, 10) * math.pow(0.8, math.floor(iter / 300))

### Generating Sequence S of +1 and -1 values###
def genrandS(n):
	S = []
	for i in range(n):
		if random.random() < 0.5:
			S.append(1)
		else:
			S.append(-1)
	return S

### Generating sequence of n values in range [1, n] ###
def genrandP(n):
	P = []
	for i in range(n):
		P.append(random.randrange(1, n))
	return P

### Generating neighbor of a solution S ###
def neighS(S):
	i = 0
	j = 0
	while (i == j):
		i = random.randrange(0, len(S))
		j = random.randrange(0, len(S))

	S[i] = -S[i]
	if random.random() < 0.5:
		S[j] = -S[j]

	return S

### Generating neighbor for prepartioning ###
def neighP(S):
	i = random.randrange(0, len(S))
	j = random.randrange(0, len(S))

	while S[i] == j:
		i = random.randrange(0, len(S))
		j = random.randrange(0, len(S))

	S[i] = j

	return S

### Residuals for sequence S ###
def residS(S, A):
	X = 0
	for i in range(len(A)): 
		if S[i] > 0: 
			X += A[i]
		else: 
			X += -A[i]
	return abs(X)

### Residuals for Prepartioning ###
def residP(S, A):
	X = [0] * len(A)
	for j in range(len(A)):
		X[S[j]] += A[j]

	return kk(X)


"""Had to use deep copy because you need to use the original Sequence
not the mutated one"""
def reprandS(A):
	S = genrandS(len(A))
	for i in range(max_iter):
		S2 = genrandS(len(A))
		if residS(S2, A) < residS(S, A):
			S = copy.deepcopy(S2)
	return residS(S, A)


def reprandP(A):
	S = genrandP(len(A))
	for i in range(max_iter):
		S2 = genrandP(len(A))
		if residP(S2, A) < residP(S, A):
			S = copy.deepcopy(S2)
	return residP(S, A)


def hillS(A):
	S = genrandS(len(A))
	for i in range(max_iter):
		S2 = neighS(copy.deepcopy(S))
		if residS(S2, A) < residS(S, A):
			S = copy.deepcopy(S2)
	return residS(S, A)

def hillP(A):
	S = genrandP(len(A))
	for i in range(max_iter):
		S2 = neighP(copy.deepcopy(S))
		if residP(S2, A) < residP(S, A):
			S = copy.deepcopy(S2)
	return residP(S, A)

def sim_annealS(A):
	S = genrandS(len(A))
	S3 = copy.deepcopy(S)
	for i in range (max_iter):
		S2 = neighS(copy.deepcopy(S))
		if residS(S2, A) < residS(S, A):
			S = copy.deepcopy(S2)
		elif random.random() < math.exp(-(residS(S2, A) - residS(S, A)) / T(i)):
			S = copy.deepcopy(S2)
		if residS(S, A) < residS(S3, A):
			S3 = copy.deepcopy(S)
	return residS(S, A)

def sim_annealP(A):
	S = genrandP(len(A))
	S3 = copy.deepcopy(S)
	for i in range (max_iter):
		S2 = neighP(copy.deepcopy(S))
		if residP(S2, A) < residP(S, A):
			S = copy.deepcopy(S2)
		elif random.random() < math.exp(-(residP(S2, A) - residP(S, A)) / T(i)):
			S = copy.deepcopy(S2)
		if residP(S, A) < residP(S3, A):
			S3 = copy.deepcopy(S)
	return residP(S, A)

### Testing ###

#### Will move this to bottom of file later ####
"""
file = open(sys.argv[1], 'r')

A = []

for line in file:
	A.append(int(line))"""

# generate 100 random instances
for i in range(100):
	X = []
	Sol = []

	for j in range(100):

		# generate set of 100 integers for testing purposes
		X.append(random.randrange(1, math.pow(10, 12)))
	
	
	Sol.append(hillS(X))
	Sol.append(hillP(X))
	Sol.append(sim_annealS(X))
	Sol.append(sim_annealP(X))
	Sol.append(reprandS(X))
	Sol.append(reprandP(X))

	Sol.append(kk(X))

	print Sol







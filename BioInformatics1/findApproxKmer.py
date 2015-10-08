import operator

def revCompl(a):
	b = a[::-1]
	res = ''
	for i in b:
		if i == 'A':
			res = res + 'T'
		elif i == 'T':
			res = res + 'A'
		elif i == 'G':
			res = res + 'C'
		elif i == 'C':
			res = res + 'G'
	return res

def HammingDistance(a,b):
	cnt = 0
	for i in range(0,len(a)):
		if a[i] != b[i]:
			cnt += 1
	return cnt


def countApproxKmer(st,kmer,d):
	cnt = 0
	for i in range(0, len(st)-len(kmer) + 1):
		if HammingDistance(kmer,st[i:i+len(kmer)]) <= d:
			cnt += 1
	return cnt

def Neighbours(patt, d):
	n = set()
	nuc = ['A','C','G','T']
	if d == 0:
		return [patt]
	if len(patt) == 1:
		return nuc
	neigh = Neighbours(patt[1:], d)
	for s in neigh:
		if HammingDistance(patt[1:],s) < d:
			for j in map(lambda x: x + s, nuc):
				n.add(j)
		else:
			n.add(patt[0] + s)
	return list(n)


def findApproxKmer(st, k, d):
	merdict = dict()
	for i in range(0, len(st)-k + 1):
		for j in Neighbours(st[i:i+k], d):
			try:
				merdict[j] += 1
			except KeyError:
				merdict[j] = 1
		for j in Neighbours(revCompl(st[i:i+k]), d):
			try:
				merdict[j] += 1
			except KeyError:
				merdict[j] = 1
	srtmer = sorted(merdict.items(), key= operator.itemgetter(1), reverse= True)
	print srtmer[0:10]
	max = 0
	kmer = []
	for j in srtmer:
		if j[1]>=max:
			kmer.append(j[0])
			max = j[1]
		else:
			break
	return kmer


if __name__ == "__main__":
	f = open('dts9.txt','r')
	st = f.read()
	st = st.replace('\n','')
	f.close()
	#st = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
	k = 7
	d = 3
	#kmer = findKmer(st,k)
	#print k,"-Mer:", kmer
	dat = findApproxKmer(st, k, d)
	f1 = open('ans_ApproxKmer.txt','w')
	dt = reduce(lambda x,y : str(x) + ' ' +str(y), dat)
	print dt
	f1.write(dt)
	f1.close()
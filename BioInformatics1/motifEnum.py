
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

def countKmer(st,kmer):
	cnt = 0
	for i in range(0, len(st)-len(kmer) + 1):
		if kmer == st[i:i+len(kmer)]:
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

def motifEnumeration(dna, k, d):
	patterns = set()
	for st in dna:
		for i in range(0, len(st)-k + 1):
			kmer = st[i:i+k]
			for j in Neighbours(kmer, d):
				flg = True
				for g in dna:
					if countApproxKmer(g,j,d) == 0:
						flg = False
						break
				if flg:
					patterns.add(j)
	return list(patterns)


if __name__ == "__main__"	:
	dna = ['ATTTGGC','TGCCTTA','CGGTATC','GAAAATT']
	f = open('dts10.txt','r')
	dat = f.read()
	dna = dat.split('\n')
	print dna
	k = 5
	d = 1
	patt = []
	patt = motifEnumeration(dna, k, d)
	patt.sort()
	dat = reduce(lambda x,y: x + ' ' + y, patt)
	print dat
	f1 = open('ans_motifEnum.txt','w')
	f1.write(dat)
	f1.close()
	f.close()
	
	
	
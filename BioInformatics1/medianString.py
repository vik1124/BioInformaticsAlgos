

def HammingDistance(a,b):
	cnt = 0
	for i in range(0,len(a)):
		if a[i] != b[i]:
			cnt += 1
	return cnt

def AllKmers(k):
	p = ['A', 'C', 'G', 'T']
	if k == 1:
		return p
	else:
		return [b+v for b in p for v in AllKmers(k-1)]

def d(patt, dna):
	k = len(patt)
	d = 0
	for st in dna:
		di = k
		for p in [st[i:i+k] for i in range(0,len(st)-k+1)]:
			di = min( HammingDistance(patt, p), di)
		d = d + di
	return d

def MedianString(dna, k):
	dist = k * len(dna)
	med = ''
	for patt in AllKmers(k):
		di = d(patt, dna)
		if di < dist:
			dist = di
			med = patt
	return med, dist

if __name__ == "__main__":
	#dna = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTTCGGGACAG']
	#dna = map(lambda x: x.upper(), dna)
	#print dna
	#print d('AAA', dna)
	f = open('dts11.txt','r')
	dat = f.read()
	f.close()
	dna = dat.split('\n')
	print dna
	k = 6
	ms, dist = MedianString(dna, k)
	print ms, dist
	f1 = open('ans_MedianString.txt','w')
	f1.write(ms)
	f1.close()
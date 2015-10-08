import operator

def clumpmer(s,k,L,t):
	merdict = dict()
	kmer = []
	srtmer= []
	for j in range(0,len(s)-L+1):
		st = s[j:j+L]
		if j == 0:
			for i in range(0, len(st)-k + 1):
				try:
					merdict[st[i:i+k]] += 1
				except KeyError:
					merdict[st[i:i+k]] = 1
			srtmer = sorted(merdict.items(), key= operator.itemgetter(1), reverse= True)
			for j in srtmer:
				if j[1]>=t:
					kmer.append(j[0])
				else:
					break
		else:
			merdict[s[j-1:j-1+k]] -= 1
			try:
				merdict[s[j+L-k:j+L]] += 1
			except KeyError:
				merdict[s[j+L-k:j+L]] = 1
			if (merdict[s[j+L-k:j+L]] >= t) and (s[j+L-k:j+L] not in kmer):
				kmer.append(s[j+L-k:j+L])
	return kmer


def findKmer(st,k,t):
	merdict = dict()
	for i in range(0, len(st)-k + 1):
		try:
			merdict[st[i:i+k]] += 1
		except KeyError:
			merdict[st[i:i+k]] = 1
	srtmer = sorted(merdict.items(), key= operator.itemgetter(1), reverse= True)
	#print srtmer[0:10]
	max = 0
	kmer = []
	for j in srtmer:
		if j[1]>=t:
			kmer.append(j[0])
			max = j[1]
		else:
			break
	return kmer


def clumps(st,k,L,t):
	cl = []
	for i in range(0,len(st) - L + 1):
		cl = cl + findKmer(st,k,t)
		cl = list(set(cl))
	return cl

def clumps1(st,k,L,t):
	cl = []
	for i in range(0,len(st) - L + 1, k):
		cl = cl + findKmer(st,k,t)
		cl = list(set(cl))
	return cl


if __name__ == "__main__":
	#f = open('dts4.txt','r')
	f = open('E-coli.txt','r')
	st = f.read()
	st = st.replace('\n','r')
	f.close()
	#st = "CACAC"
	k = 9
	L = 500
	t = 3
	cl = clumpmer(st,k,L,t)
	cl = list(set(cl))
	d = reduce(lambda x,y: str(x) + " " + str(y), cl)
	print "Clump Algo:", d
	#cl = clumps(st,k,L,t)
	#d = reduce(lambda x,y: str(x) + " " + str(y), cl)
	f1 = open('ans_clumpmer_ecoli.txt','w')
	f1.write(d)
	f1.close()
	#print d
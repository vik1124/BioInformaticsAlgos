def ProbabilityScore(patt, profile):
	bp = ['A', 'C', 'G', 'T']
	sc = 1.0
	for i in range(len(patt)):
		p = patt[i]
		sc = sc * profile[bp.index(p)][i]
	return sc


def ProbableKmer(st, k, pr):
	sc = 0.0
	pt = ''
	for p in [st[i:i+k] for i in range(0, len(st) - k + 1)]:
		psc = ProbabilityScore(p, pr)
		if psc > sc:
			sc = psc
			pt = p
	return pt, sc


def genProfileLaplace(patts):
	t = len(patts) + 4
	bp = ['A', 'C', 'G', 'T']
	#print patts
	profile = [[0]*len(patts[0]) for j in bp]
	for i in range(0, len(patts[0])):
		for j in patts:
			profile[bp.index(j[i])][i] += 1.0/t
	for i in range(len(bp)):
		for j in range(len(patts[0])):
			profile[i][j] += 1.0/t
	return profile[:]


def greedyMotifSearch(dna, k):
	bestPatts = []
	for i in dna:
		bestPatts.append(i[:k])
	profile = genProfileLaplace(bestPatts)
	#print profile
	#print bestPatts
	bestsc = sum(map(lambda x: ProbabilityScore(x, profile), bestPatts))
	print "Best Score:", bestsc
	for kmer in [dna[0][i:i+k] for i in range(0,len(dna[0]) - k + 1)]:
		patts = [kmer]
		score = 0.0
		for j in range(1, len(dna)):
			profile = genProfileLaplace(patts)
			pt, sc = ProbableKmer(dna[j], k, profile)
			score += sc
			if pt == '':
				patts.append(dna[j][:k])
			else:
				patts.append(pt)
		#print "for ", kmer, " score:", score, " Motifs: ", patts #, " profile: ", profile
		#print "score ", kmer, ": ", score
		if score > bestsc:
			print "score ", kmer, ": ", score
			bestsc = score
			bestPatts = patts
	return bestPatts, bestsc




if __name__ == "__main__":
	f = open('dts14.txt', 'r')
	dat = f.read()
	f.close()
	dna = dat.split('\n')
	k = 12
	motifs, score = greedyMotifSearch(dna, k)
	st = ''
	for i in motifs:
		print i
		st = st + i + '\n'
	print score
	f1 = open('ans_greedyMotifSearchLaplace.txt','w')
	f1.write(st)
	f1.close()
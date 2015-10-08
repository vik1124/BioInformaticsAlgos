from random import *

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
	#for i in dna:
	#	n = randint(0, len(i) - k)
	#	bestPatts.append(i[n:n+k])
	bestPatts = ['GTC','CCC','ATA','GCT']
	profile = genProfileLaplace(bestPatts)
	print profile
	print bestPatts
	bestsc = sum(map(lambda x: ProbabilityScore(x, profile), bestPatts))
	print "Best Score:", bestsc
	cnt = 0
	while 1:
		cnt = cnt + 1
		profile = genProfileLaplace(bestPatts)
		patts = []
		score = 0.0
		for j in range(0, len(dna)):
				pt, sc = ProbableKmer(dna[j], k, profile)
				score += sc
				patts.append(pt)
		#print "for ", kmer, " score:", score, " Motifs: ", patts #, " profile: ", profile
		#print "score ", kmer, ": ", score
		print "Count: ", cnt, " patts: ", patts, " score: ", score
		if score > bestsc:
			#print "score: ", score
			bestsc = score
			bestPatts = patts
		else:
			return bestPatts, bestsc
	return None, None


def IterativeSearch(dna, k, val):
	bestPatts, patts = [], []
	bestScore, score = 0.0, 0.0
	bestPatts, bestScore = greedyMotifSearch(dna, k)
	for i in range(val-1):
		patts, score = greedyMotifSearch(dna, k)
		if score >  bestScore:
			print "score: ", score
			bestScore = score
			bestPatts = patts
	return bestPatts, bestScore




if __name__ == "__main__":
	f = open('dts17.txt', 'r')
	dat = f.read()
	f.close()
	dna = dat.split('\n')
	k = 3
	motifs, score = greedyMotifSearch(dna, k)
	#motifs, score =  IterativeSearch(dna, k, 1000)
	st = ''
	for i in motifs:
		print i
		st = st + i + '\n'
	print score
	f1 = open('ans_RandomMotifSearchLaplace_quiz.txt','w')
	f1.write(st)
	f1.close()
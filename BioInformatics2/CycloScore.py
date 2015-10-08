

IntMassDict = dict()

def genIntMass():
	global IntMassDict
	f = open('IntegerMassTable.txt','r')
	dat = f.read()
	tab = dat.split('\n')
	for i in tab:
		v = i.split(' ')
		IntMassDict[v[0]] = int(v[1])
	print IntMassDict

def CycloSpectrum(patt):
	p = [0]
	k = len(patt)
	patt = patt + patt
	weights = [IntMassDict[i] for i in patt]
	for i in range(1, k):
		p += [sum(weights[j:j+i]) for j in range(k)]
	p += [sum(weights[:-k])]
	p.sort()
	return p

def score(patt, seq):
	theoSeq = CycloSpectrum(patt)
	i, score, k = 0, 0, len(theoSeq)
	for i in theoSeq:
		if i in seq:
			score += 1
			seq.remove(i)
	return score


if __name__ == "__main__":
	f = open('dts16.txt', 'r')
	dat = f.read()
	f.close()
	dat = dat.replace('\n','')
	seq = map(lambda x: int(x), dat.split(' '))
	genIntMass()
	patt = 'LCQSCRRCKHLAAWDEIGEYAAILQFFSNIKAWRHL'
	sc = score(patt, seq)
	print sc
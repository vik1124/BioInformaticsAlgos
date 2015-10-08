import time
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

def CycloSpectrum1(patt):
	pm  = [0]
	for i in patt:
		pm.append(pm[-1] + IntMassDict[i])
	#print "PrefixMass: ", pm
	p = [0]
	for i in range(0, len(pm)-1):
		for j in range(i+1, len(pm)):
			p.append(pm[j] - pm[i])
			if i>0 and j<len(patt):
				p.append( pm[-1] - (pm[j] - pm[i]))
	p.sort()
	return p

def Mass(spect):
	mass = 0
	for i in spect:
		mass += IntMassDict[i]
	return mass

def CycloPeptideSequencing(seq):
	pep = IntMassDict.keys()
	p = pep[:]
	op = []
	while len(p)>0:
		for i in p[:]:
			if Mass(i) not in seq:
				p.remove(i)
			elif CycloSpectrum1(i) == seq:
				op.append(i)
				p.remove(i)
		if len(p) > 0:
			print len(p[-1]), len(p)
			if len(p[-1]) == 1:
				pep = p[:]
				print pep
			for i in p[:]:
				p = p + [i+j for j in pep]
				p.remove(i)
	op.sort()
	return op
	
	

if __name__ == "__main__":
	a= time.time()
	f = open('dts15.txt', 'r')
	dat = f.read()
	f.close()
	dat = dat.replace('\n','')
	seq = map(lambda x: int(x), dat.split(' '))
	genIntMass()
	#c= time.time()
	#cd = CycloSpectrum1('MPYENCCCWMFNIRKGQPDFFRKGAVPYVVPMNCIRWS')
	#d = time.time()
	#de = CycloSpectrum('MPYENCCCWMFNIRKGQPDFFRKGAVPYVVPMNCIRWS')
	#e = time.time()
	#print cd==de
	#print "CycloSpectrum1 took:", d-c
	#print "CycloSpectrum took:", e-d
	op = CycloPeptideSequencing(seq)
	OutputSeq = [reduce(lambda x, y : x+'-'+y, map(lambda x: str(IntMassDict[x]), i)) for i in op]
	OutputSeq = list(set(OutputSeq))
	f1 = open('ans_CycloPeptideSequencing.txt','w')
	f1.write( reduce(lambda x,y: x + ' ' +y, OutputSeq ) )
	f1.close()
	b = time.time()
	print "Took: ", b-a
	
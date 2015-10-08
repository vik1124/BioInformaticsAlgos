
AADict = dict()

def genAAdict():
	global AADict 
	f = open('AminoAcidWeights.txt', 'r')
	dat = f.read()
	aa = dat.split('\n')
	for i in aa:
		v = i.split(' ')
		AADict[v[0]] = int(v[1])
	print AADict

def TheoSpectrum(patt):
	w = map(lambda x: AADict[x], patt)
	spect  = [0]
	k = len(patt)
	w = w + w
	for i in range(1, k):
		q = [sum(w[j:j+i]) for j in range(0,k)]
		spect += q
	spect.append(sum(w)/2)
	return spect



if __name__ == "__main__":
	genAAdict()
	patt = 'GVYEKRIMSMKHMEP'
	spect = TheoSpectrum(patt)
	print spect
	spect.sort()
	f1 = open('ans_theospectrum.txt', 'w')
	f1.write(reduce(lambda x,y: str(x)+ ' '+str(y), spect))
	f1.close()

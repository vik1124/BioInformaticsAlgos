from translate import *


def revComplRNA(a):
	b = a[::-1]
	res = ''
	for i in b:
		if i == 'A':
			res = res + 'U'
		elif i == 'U':
			res = res + 'A'
		elif i == 'G':
			res = res + 'C'
		elif i == 'C':
			res = res + 'G'
	return res

def findSubsstrings(dat, seq):
	k = len(seq) * 3
	subst = [ dat[i:i+k] for i in range(0,len(dat)-k+1) ]
	strings = []
	for i in subst:
		j = i.replace('T','U')
		if translate(j) == seq or translate(revComplRNA(j)) == seq :
			strings.append(i)
	return strings
	

if __name__ == "__main__":
	f = open('dts12.txt', 'r')
	dat = f.read()
	dat = dat.replace('\n','')
	genRNACodonDict()
	seq = 'AHHQQRCD'
	substrings = findSubsstrings(dat, seq)
	f1 = open('ans_Substrings.txt','w')
	f1.write(reduce(lambda x,y: x + '\n' + y, substrings))
	f1.close()
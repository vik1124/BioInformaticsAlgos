


def minSkew(st):
	sk = []
	minInd = []
	minVal = 0
	n = 0
	for i in range(0,len(st)):
		sk.append(n)
		if st[i] == 'G':
			n += 1
		elif st[i] == 'C':
			n -= 1
		if n < minVal:
			minVal = n
	sk.append(n)
	for i in range(0,len(sk)):
		if sk[i] == minVal:
			minInd.append(i)
	return minInd

def skew(st):
	sk = []
	n = 0
	for i in range(0,len(st)):
		sk.append(n)
		if st[i] == 'G':
			n += 1
		elif st[i] == 'C':
			n -= 1
	sk.append(n)
	return sk

if __name__ == "__main__":
	a = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
	#f = open('dts5.txt','r')
	f = open('salmonella_enterica.txt','r')
	a = f.read()
	f.close()
	a = a.replace('\n','')
	sk = skew(a)
	#print sk
	q = ''
	ms = minSkew(a)
	f1 = open('ans_skew_min_salmonella.txt','w')
	for i in ms:
		q = q + str(i) + ' '
	print q
	f1.write(q)
	f1.close()
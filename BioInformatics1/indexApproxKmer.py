

def hammingDistance(a,b):
	cnt = 0
	for i in range(0,len(a)):
		if a[i] != b[i]:
			cnt += 1
	return cnt


def indexApproxKmer(st,kmer,d):
	cnt = []
	for i in range(0, len(st)-len(kmer) + 1):
		if hammingDistance(kmer,st[i:i+len(kmer)]) <= d:
			cnt.append(i)
	return cnt


if __name__ == "__main__":
	f = open('dts7.txt','r')
	st = f.read()
	st = st.replace('\n','')
	f.close()
	f1 = open('ans_approx_Kmer.txt','w')
	#st = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
	kmer = "CAGCAAGTTGA"
	d = 6
	c = indexApproxKmer(st, kmer, d)
	dat = reduce(lambda x,y: str(x) + " " + str(y), c)
	print dat
	f1.write(dat)
	f1.close()




def hammingDistance(a,b):
	cnt = 0
	for i in range(0,len(a)):
		if a[i] != b[i]:
			cnt += 1
	return cnt

def countApproxKmer(st,kmer,d):
	cnt = 0
	for i in range(0, len(st)-len(kmer) + 1):
		if hammingDistance(kmer,st[i:i+len(kmer)]) <= d:
			cnt += 1
	return cnt


if __name__ == "__main__":
	f = open('dts8.txt','r')
	st = f.read()
	st = st.replace('\n','r')
	f.close()
	#st = "TTTAGAGCCTTCAGAGG"
	kmer = "GCCCGC"
	d = 2
	c = countApproxKmer(st,kmer, d)
	print c
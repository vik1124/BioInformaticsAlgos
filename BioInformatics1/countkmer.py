

def countKmer(st,kmer):
	cnt = 0
	for i in range(0, len(st)-len(kmer) + 1):
		if kmer == st[i:i+len(kmer)]:
			cnt += 1
	return cnt


if __name__ == "__main__":
	f = open('dts1.txt','r')
	st = f.read()
	st = st.replace('\n','r')
	f.close()
	st = "GACCATCAAAACTGATAAACTACTTAAAAATCAGT"
	kmer = "AAA"
	c = countKmer(st,kmer)
	print c
	
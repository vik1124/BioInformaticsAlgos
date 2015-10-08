
def indexKmer(st,kmer):
	cnt = []
	for i in range(0, len(st)-len(kmer) + 1):
		if kmer == st[i:i+len(kmer)]:
			cnt.append(i)
	return cnt


if __name__ == "__main__":
	#f = open('dts3.txt','r')
	f = open('vibrio_cholerae.txt','r')
	st = f.read()
	st = st.replace('\n','')
	f.close()
	#f1 = open('ans2.txt','w')
	f1 = open('ans_Vibrio_Cholerae.txt','w')
	#st = "GCGCG"
	kmer = "CTTGATCAT"
	c = indexKmer(st,kmer)
	d = reduce(lambda x,y: str(x) + " " + str(y), c)
	f1.write(d)
	f1.close()
	#print d
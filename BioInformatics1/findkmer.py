import operator

def findKmer(st,k):
	merdict = dict()
	for i in range(0, len(st)-k + 1):
		try:
			merdict[st[i:i+k]] += 1
		except KeyError:
			merdict[st[i:i+k]] = 1
	srtmer = sorted(merdict.items(), key= operator.itemgetter(1), reverse= True)
	print srtmer[0:10]
	max = 0
	kmer = []
	for j in srtmer:
		if j[1]>=max:
			kmer.append(j[0])
			max = j[1]
		else:
			break
	return kmer


if __name__ == "__main__":
	#f = open('dts2.txt','r')
	f = open('vibrio_cholerae.txt','r')
	st = f.read()
	st = st.replace('\n','')
	st = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
	f.close()
	#st = "CACAC"
	k = 3
	kmer = findKmer(st,k)
	print k,"-Mer:", kmer


def ProbabilityScore(patt, profile):
	bp = ['A', 'C', 'G', 'T']
	sc = 1.0
	for i in range(len(patt)):
		p = patt[i]
		sc = sc * profile[bp.index(p)][i]
	return sc


def ProbableKmer(st, k, pr):
	sc = 0.0
	pt = ''
	for p in [st[i:i+k] for i in range(0, len(st) - k + 1)]:
		psc = ProbabilityScore(p, pr)
		if psc > sc:
			sc = psc
			pt = p
	return pt, sc


if __name__ == "__main__":
	f = open('dts12.txt','r')
	dat = f.read()
	dat = dat.split('\n')
	pr = [list(eval(i.replace(' ',','))) for i in dat]
	print pr
	patt = 'GGGAGAGCGATTCAGAGACTCGCCGGGGCCATCTGCGGGCACACATATCATAGGGCCTCCTACCCTAGTCTGTTTGAGCAACGAGTCGAAACACTCTCGAATTACAGAAGCCGTCCCAGCATTAGCGGTGTAAGACCTTCATAATAGACGCCAAGGGAATGCCTGTCTGCTATTGATGTTGTTTTCTACGGCGAACTCTGGATGATATAATTTAGATATTGCTCTCGAGTATGTTTGAACTGCTTTTTTAGCATTCTGTATTGCTTAGTCGCACCTGAGCACGACTTTTAAGGTAAATATTGAGCCTCTCGTCTTTAGAAGTAGCAAAGTTATGACAATCTGCCCTTGTACCAGGTCCCGTGCTAGGTGACAATATGCTGCTTCCTCCGAGGACACGTGAACAGCGGCCCGCCGGCTGCGATATTAACGGTGAAGTAAAAGTCACAATTTGGTCCCACTTCGATGACCTCTGAGAGAAATCTTATAAGACACACTCGGCCATGATACTTGAACCAATGATTCATGTTGTACCTTACTCGCGTAGGCGGACTAACGTACCGTGGCTGAATAAGCCCACTCCTACACTGTTTGTTCCAGGGATGCTGATCATCACAGCTAGAATTGTTTCGTAATCTGCAAATGACTGCGCCAGTCCGCCTTTTCGATGGATATTCTGTTCGTACGGATCAGGAAACGCTGACGATCAGGCGATACGGTGACACATTCGTCTCGTATTTCTGTGATAGATAATAGCTGGCGTTGTTTTGGATTGCTACAAAACTCGTCCGACCAGGATCACATCACAGAATGGCGGATTAGTGACACTCCCAGAGGGGGGTGCCTTCTGACACTCCTGACCGCATCTATCGTAGCGATCGTTGAGTGGTGCGGTCCCTGATTCGTTGCCGTCAAGTGTTCCACGCGGATGTTCATGGGTAACGGGATCCAGATTCTGAAAGCTTGGCGCGGACACCCGTCCTCGGAGGGAACGATGGTAAGT'
	k = 15
	pt, sc = ProbableKmer(patt, k, pr)
	print pt, sc
	f1 = open('ans_probableKmer.txt','w')
	f1.write(pt)
	f1.close()
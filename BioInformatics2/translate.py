
RNACodonDict = dict()

def genRNACodonDict():
	global RNACodonDict
	f = open('RNA_codon_table.txt', 'r')
	dat = f.read()
	RNACodon = dict()
	c = dat.split('\n')
	for i in c:
		v = i.split(' ')
		RNACodon[v[0]] = v[1]
	#print RNACodon
	RNACodonDict = RNACodon

def translate(rna):
	codons = [rna[3*i:3*i+3] for i in range(len(rna)/3)]
	aminoacidstring = ''
	for i in codons:
		aminoacidstring += RNACodonDict[i]
	return aminoacidstring



if __name__ == "__main__":
	f = open('dts11.txt', 'r')
	dat = f.read()
	rna = dat.replace('\n','')
	genRNACodonDict()
	aminoacidstring = translate(rna)
	f1 = open('ans_Translate.txt','w')
	f1.write(aminoacidstring)
	f1.close()
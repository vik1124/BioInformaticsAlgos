from collections import *

def DeBrujin(dna, k):
	k = k - 1
	kmers = [dna[i:i+k] for i in range(0,len(dna) - k + 1)]
	print "Number of Kmers: ", len(kmers)
	adj = defaultdict(list)
	for i in range(0,len(kmers) - 1):
		adj[kmers[i]].append(kmers[i+1])
	print len(adj)
	return adj

if __name__ == "__main__":
	f = open('dts4.txt', 'r')
	dat = f.read()
	dat = dat.replace('\n','')
	k = 12
	adj = DeBrujin(dat, k)
	#print adj
	st = ''
	adjKeys = adj.keys()
	adjKeys.sort()
	for i in adjKeys:
			adj[i].sort()
			st = st + i + ' -> ' + reduce( lambda x, y: x + ',' + y ,  adj[i]) + '\n'
	print st
	f1 = open('ans_DeBrujin.txt','w')
	f1.write(st)
	f1.close()
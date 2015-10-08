from collections import *

def deBruijinPatts(patterns):
	print "Number of patterns: ", len(patterns)
	adj = defaultdict(list)
	for i in patterns:
		adj[i[:-1]].append(i[1:])
	print len(adj)
	return adj

if __name__ == "__main__":
	f = open('dts5.txt', 'r')
	dat = f.read()
	patts = dat.split('\n')
	k = 12
	adj = deBruijinPatts(patts)
	#print adj
	st = ''
	adjKeys = adj.keys()
	adjKeys.sort()
	for i in adjKeys:
			adj[i].sort()
			st = st + i + ' -> ' + reduce( lambda x, y: x + ',' + y ,  adj[i]) + '\n'
	print st
	f1 = open('ans_DeBrujinPatterns.txt','w')
	f1.write(st)
	f1.close()
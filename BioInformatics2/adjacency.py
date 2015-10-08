

def adjacency(kmers):
	k = len(kmers[0])
	print k
	print len(kmers)
	adj = dict()
	for i in range(0,len(kmers)):
		st = kmers[i]
		for j in kmers:
			if st[-(k-1):] ==  j[:k-1]:
				try:
					adj[st].append(j)
				except KeyError:
					adj[st] = [j]
	print len(adj)
	return adj

if __name__ == "__main__":
	f = open('dts3.txt', 'r')
	dat = f.read()
	kmers = dat.split('\n')
	adj = adjacency(kmers)
	st = ''
	adjKeys = adj.keys()
	adjKeys.sort()
	for i in adjKeys:
		for j in adj[i]:
			st = st + i + ' -> ' + j + '\n'
	print st
	f1 = open('ans_Adjacency.txt','w')
	f1.write(st)
	f1.close()
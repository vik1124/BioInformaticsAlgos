

from collections import *

def arrangeNodes(a,b):
	return str([min(a,b), max(a,b)])

adj = defaultdict(list)

def genEdgeSet(cycle):
	v = set()
	for i in range(0,len(cycle)-1):
		v.add(arrangeNodes(cycle[i], cycle[i+1]))
	return v

def find_all_paths(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if not graph.has_key(start):
		return []
	paths = []
	for node in graph[start]:
		if node not in path:
			newpaths = find_all_paths(graph, node, end, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths

def EulerWalk(cycles, n):
	te = sum(map(lambda x: len(x), adj.values()))
	print "TotalEdges:", te
	v = set()
	p = []
	a = defaultdict(list)
	for i in cycles:
		a[i[0]].append(i)
	print a
	k = a[n][0]
	l = len(k)
	v = genEdgeSet(k)
	while len(v) < te:
		for i in range(0,l-1):
			if len(k) != l :
				v = genEdgeSet(k)
				l = len(k)
				break
			for j in a[k[i]]:
				v1 = genEdgeSet(j)
				if len(v.intersection(v1)) == 0:
					v = v.union(v1)
					del k[i]
					k = k[:i] + j + k[i:]
					break
	return k
	

def getCycles():
	paths = []
	s = set()
	for i in adj.keys():
		p = []
		for j in adj[i]:
			p = p + find_all_paths(adj, j, i)
		for k in range(0,len(p)):
			p[k].insert(0, i)
		#print p
		paths = paths + p
	return paths


def genGraph(patts):
	global adj
	maxcnt = 0
	n = 0
	for i in patts:
		cnt = 0
		v = i.split(' -> ')
		for j in eval('['+v[1]+']'):
			cnt += 1
			adj[int(v[0])].append(j)
		if cnt > maxcnt:
			maxcnt = cnt
			n = int(v[0])
	return adj, n


if __name__ == "__main__":
	f = open('dts6.txt', 'r')
	dat = f.read()
	patts = dat.split('\n')
	adj, n = genGraph(patts)
	print "Graph:", adj
	print "Node with max edges: ", n
	paths, st = [], ''
	cycles = getCycles()
	print cycles
	k = EulerWalk(cycles, n)
	st = reduce( lambda x, y: str(x) + '->' + str(y) ,  k)
	print st
	f1 = open('ans_EulerCycle.txt','w')
	f1.write(st)
	f1.close()
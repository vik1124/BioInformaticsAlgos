

from collections import *

def arrangeNodes(a,b):
	return str([min(a,b), max(a,b)])

adj = defaultdict(list)

def genEdgeSet(cycle):
	v = set()
	for i in range(0,len(cycle)-1):
		v.add(arrangeNodes(cycle[i], cycle[i+1]))
	return v

def find_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if not graph.has_key(start):
		return []
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path)
			if newpath:
				return newpath
	return None

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


def EulerWalk(cycles, path):
	te = sum(map(lambda x: len(x), adj.values()))
	print "TotalEdges:", te
	v = set()
	p = []
	a = defaultdict(list)
	for i in cycles:
		a[i[0]].append(i)
	print a
	k = path
	l = len(k)
	v = genEdgeSet(k)
	while len(v) < te:
		#print "k:", k
		for i in range(0,l):
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


def getDegree():
	a = defaultdict(int)
	for i in adj.keys():
		a[i] = (len(adj[i]))
	for j in adj.values():
		for k in j:
			if k in a.keys():
				a[k] -= 1
			else:
				a[k] = -1
	return a

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
	return adj


if __name__ == "__main__":
	f = open('dts7.txt', 'r')
	dat = f.read()
	patts = dat.split('\n')
	adj = genGraph(patts)
	print "Graph:", adj
	paths, st = [], ''
	deg = getDegree()
	end = [i for i in deg.keys() if deg[i] < 0]
	start = [i for i in deg.keys() if deg[i] > 0]
	print "start:", start, " End;", end
	path = find_path(adj, start[0], end[0])[0]
	print "path:", path
	cycles = getCycles()
	print cycles
	walk = EulerWalk(cycles, path)
	st = reduce( lambda x, y: str(x) + '->' + str(y) ,  walk)
	print st
	f1 = open('ans_EulerWalk.txt','w')
	f1.write(st)
	f1.close()
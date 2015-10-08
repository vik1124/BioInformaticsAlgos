

def reconstruct(kmers):
	k = len(kmers[0])
	print k
	print len(kmers)
	st = kmers[0]
	for i in range(1,len(kmers)):
		if st[-(k-1):] ==  kmers[i][:k-1]:
			st = st + kmers[i][-1]
	print len(st)
	return st

if __name__ == "__main__":
	f = open('dts2.txt', 'r')
	dat = f.read()
	kmers = dat.split('\n')
	st = reconstruct(kmers)
	print st
	f1 = open('ans_Reconstruction.txt','w')
	f1.write(st)
	f1.close()


if __name__ == "__main__":
	f = open('dts1.txt', 'r')
	dat = f.read()
	dat = dat.replace('\n','')
	k = 100
	kmers = [dat[i:i+k] for i in range(0,len(dat) - k + 1)]
	st = reduce(lambda x,y: x + '\n' + y, kmers)
	print st
	f1 = open('ans_Composition.txt','w')
	f1.write(st)
	f1.close()
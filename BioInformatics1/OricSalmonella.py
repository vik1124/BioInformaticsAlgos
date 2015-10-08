from findApproxKmer import *
from skew import *

def oricSalmonella():
	f = open('salmonella_enterica.txt','r')
	a = f.read()
	f.close()
	a = a.replace('\n','')
	sk = skew(a)
	ms = minSkew(a)
	print ms
	minInd = ms[0]
	print "Oric Starting Point chosen: ", minInd
	st = a[minInd:minInd+1000]
	k = 9
	d = 1
	dat = findApproxKmer(st, k, d)
	print dat
	f1 = open('ans_oric_Salmonella.txt','w')
	dt = reduce(lambda x,y : str(x) + ' ' +str(y), dat)
	print dt
	f1.write(dt)
	f1.close()


if __name__ == "__main__":
	oricSalmonella()
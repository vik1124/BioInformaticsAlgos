

def hammingDistance(a,b):
	cnt = 0
	for i in range(0,len(a)):
		if a[i] != b[i]:
			cnt += 1
	return cnt


if __name__ == "__main__":
	a = 'GGGCCGTTGGT'
	b = 'GGACCGTTGAC'
	f = open('dts6.txt','r')
	a = f.readline()
	b = f.readline()
	a = a.strip()
	b = b.strip()
	print hammingDistance(a,b)
	
	
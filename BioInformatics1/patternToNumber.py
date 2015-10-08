
pn = {'A':0, 'C':1, 'G':2, 'T':3}
np = {0:'A', 1:'C', 2:'G', 3:'T'}

def patternToNumber(s):
	if len(s) > 1:
		return 4 * patternToNumber(s[:-1]) + pn[s[-1]]
	else:
		return pn[s]

def numberToPattern(n):
	if n//4 != 0:
		return numberToPattern(n//4) + np[n%4]
	else:
		return np[n%4]


if __name__ == "__main__":
	#print patternToNumber('CATATCTCAAGACGTC')
	print numberToPattern(8540)
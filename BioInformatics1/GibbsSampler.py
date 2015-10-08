from random import *

"""
Code Calculates possible motifs using the Gibb's Sampler Algorithm for a given set of Dna strings
"""

def ProbabilityScore(patt, profile):
    bp = ['A', 'C', 'G', 'T']
    sc = 1.0
    for i in range(len(patt)):
        p = patt[i]
        sc = sc * profile[bp.index(p)][i]
    return sc


def WeightedRandomKmer(st, k, pr):
    sc = 0.0
    psc = []
    kmers = [st[i:i+k] for i in range(0, len(st) - k + 1)]
    for p in kmers:
        psc.append(ProbabilityScore(p, pr))
    tot = sum(psc)
    #print "total:",tot
    #print "psc: ", psc
    weightedRandom = uniform(0.0, tot)
    for i in range(0, len(psc)):
        sc += psc[i]
        if sc >= weightedRandom:
            #print "w Rand:", i, " score:",psc[i]
            return kmers[i]
    return kmers[-1]


def genProfileLaplace(patts):
    t = len(patts) + 4
    bp = ['A', 'C', 'G', 'T']
    #print patts
    profile = [[0]*len(patts[0]) for j in bp]
    for i in range(0, len(patts[0])):
        for j in patts:
            profile[bp.index(j[i])][i] += 1.0/t
    for i in range(len(bp)):
        for j in range(len(patts[0])):
            profile[i][j] += 1.0/t
    return profile[:]


def GibbsSamplerSearch(dna, k, N):
    bestPatts = []
    for i in dna:
        n = randint(0, len(i) - k)
        bestPatts.append(i[n:n+k])
    profile = genProfileLaplace(bestPatts)
    #print profile
    #print bestPatts
    pt = ''
    bestsc = sum(map(lambda x: ProbabilityScore(x, profile), bestPatts))
    patts = bestPatts[:]
    #print "Best Score:", bestsc
    for q in range(N):
        i = randint(0, len(dna) - 1)
        patts.remove(patts[i])
        score = 0.0
        profile = genProfileLaplace(patts)
        pt = WeightedRandomKmer(dna[i], k, profile)
        patts.insert(i, pt)
        score = sum(map(lambda x: ProbabilityScore(x, profile), patts))
        #print "for ", kmer, " score:", score, " Motifs: ", patts #, " profile: ", profile
        #print "score ", kmer, ": ", score
        if score > bestsc:
            #print "score: ", score
            bestsc = score
            bestPatts = patts
    return bestPatts, bestsc


def IterativeSearch(dna, k, N, val):
    bestPatts, patts = [], []
    bestScore, score = 0.0, 0.0
    bestPatts, bestScore = GibbsSamplerSearch(dna, k, N)
    for i in range(val-1):
        patts, score = GibbsSamplerSearch(dna, k, N)
        if score > bestScore:
            print "Iterative Search Score: ", score
            bestScore = score
            bestPatts = patts
    return bestPatts, bestScore




if __name__ == "__main__":
    f = open('dts16.txt', 'r')
    dat = f.read()
    f.close()
    dna = dat.split('\n')
    k = 20
    N = 2000
    motifs, score = IterativeSearch(dna, k, N, 20)
    st = ''
    for i in motifs:
        print i
        st = st + i + '\n'
    print score
    f1 = open('ans_GibbsSamplerSearchLaplace.txt', 'w')
    f1.write(st)
    f1.close()

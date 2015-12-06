import sys 

OUTNM = 'knowfact_corpus_v4.txt'
#FILENM = "D:/Study/OpenInfoExtraction/corpus/spanish_corpus_v3.txt"
FILENM = "D:/Study/OpenInfoExtraction/corpus/spanish_corpus_v3_and_noFrench.txt"


def main (argv):
    if len(argv) != 1:
        sys.stderr.write('Usage: %s wrong usage! \n' % argv[0])
        sys.exit(-1)
    
    f = open(FILENM)
    fout = open(OUTNM, 'w')
    
    j = 0
    m = 0  
    for s in f: 
      if s.strip() == '' or s.strip() == ' ': 
        print 'vacia'
        continue 
      elif s.strip()[0] == '#': 
         print '#'
         i = 0 
      else: 
        i+=1
        j+=1
        if i == 2: 
         print s 
         print >>fout, s.strip() 
         m +=1
    
    f.close()
    fout.close()     
    print "Total # of sentences: ", j
    print "Total # of sentences in a corpus: ", m
    
 
if __name__ == '__main__':
    main(sys.argv)
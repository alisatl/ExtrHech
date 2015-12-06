import os 
import sys

OUTEXT = '_lined.pos'

SENTFN = "D:\Study\OpenInfoExtraction\corpus\knowfact_corpus_v4.txt"
OUTFN = "D:\Study\OpenInfoExtraction\corpus\ExtrHech_outputs\knowfact_v4_final.facts"
INFN = "D:\Study\OpenInfoExtraction\corpus\ExtrHech_outputs\knowfact_v4.facts"

def main(argv):
    '''
    if len(argv) != 2:
        sys.stderr.write("Usage: %s POStagged_file" % argv[0])
        sys.exit(-1)
    
    file = argv[1]
    print file
    '''
    
    f_sent = open(SENTFN)
    fout = open(OUTFN, 'w')
    
    for s in open(INFN):  
      fout.write(s.strip()+'\n')
      if s.strip() == '###############':
        fout.write(f_sent.readline().strip()+'\n')
    fout.close()    

if __name__ == "__main__":
    main(sys.argv)
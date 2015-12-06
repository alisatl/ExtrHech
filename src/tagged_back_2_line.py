import os 
import sys

###################################################################################
#  gets back a tagged sentence splitted word-per-line (after Freeling) back to line
#
#  USAGE: 
#  tagged_back_2_line.py file_splitted_per_line
#
#  OUTPUT: 
#
#  file_splitted_per_line_LINED.pos
###################################################################################


OUTEXT = '_LINED.pos'

#OUTPATH ="D:/Study/OpenInfoExtraction/50docs/numbered/pos/lined/"
OUTPATH ="D:/Study/OpenInfoExtraction/corpus/POS-tagged/ISO_lined"

def get_labels(path):  
    labels = {}
    print "Reading pair labels ..."
    # for each subcategory file in a directory 
    for fi in os.listdir(path):
        #print fi
        full_name = os.path.join(path, fi)
        fnPairs = full_name
        ch = fi[fi.rfind('-')+1:fi.find('.txt')]
        for ln in open(fnPairs):
            pair = ln.strip()
            if pair not in labels: 
              labels[pair] = [ch]
            else:  
              labels[pair].append(ch)
    
    return labels 



def main(argv):
    if len(argv) != 2:
        sys.stderr.write("Usage: %s POStagged_file" % argv[0])
        sys.exit(-1)
    
    file = argv[1]
    print file
    
    filenm = file[:file.find('.')]
    
    #ch = file[file.rfind('/')+1:file.find('_')]
    
    #filenm_out = OUTPATH+ ch + OUTEXT
    filenm_out = filenm + OUTEXT
    
    print  filenm_out
    
    fout = open(filenm_out, 'w')
        
    sent = []
    
    for s in open (file):  
      if s.strip() == '':
        print "THis is an empty line" 
        if sent !=[]:
          print >> fout, ' '.join(s.strip() for s in sent if len(s.strip()) != 0)
        sent = []
        continue 
      ws = s.strip().split()
      #print s 
      #print ws 
      word = ws[0]+'^'+ws[1]+'^'+ws[2]
      sent.append(word)
      #print sent
      
    fout.close()   
     

    #labels = get_labels(path)
    """
    print "Printing out the results to: ", OUTNM
    fout = open(OUTNM, 'w')
    for pair in labels: 
         print >>fout, pair, '\t', labels[pair]
    fout.close() 
    """

if __name__ == "__main__":
    main(sys.argv)
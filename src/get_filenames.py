import os 
import sys

OUTNM = 'file_name_correspondence.txt'


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

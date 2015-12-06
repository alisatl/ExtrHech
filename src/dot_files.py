import os 
import sys

PATH = '/cygdrive/d/Study/OpenInfoExtraction/50docs/numbered/'

PATH2 = '/cygdrive/d/Study/OpenInfoExtraction/50docs/original/'

TAG = '_dotted.txt'


def get_labels(path):  
    #labels = {}
    print "Reading files ..."
    # for each file in a directory 
    for fi in os.listdir(path):
        print fi
        full_name = os.path.join(path, fi)
        ch = fi[fi.rfind('/')+1:fi.find('.txt')]
        outnm = ch+TAG
        fout = open(outnm, 'w')
        for ln in open(full_name): 
            line = ln.strip() +'.'
            print >>fout, line
        fout.close()
    #return labels 

#get_labels(PATH)

def count_lines(path):  
    # for each file in a directory 
    for fi in os.listdir(path):
        chars = 0 
        lines = 0 
        full_name = os.path.join(path, fi)
        for ln in open(full_name):
            lines +=1
            ln = ln.strip()
            s = ln.replace(' ', '')   
            chars +=len(s)
        print chars, lines      

count_lines(PATH2)



#def main (argv):
#    if len(argv) != 3:
#        sys.stderr.write('Usage: %s Config_file POS_tagged_file \n' % argv[0])
#        sys.exit(-1)
        
        
        
        
#if __name__ == '__main__':
#    main(sys.argv)        
import sys

def main (argv):
    if len(argv) != 3:
        sys.stderr.write('Usage: %s file1 file2 \n' % argv[0])
        sys.exit(-1)
    
    filenm1, filenm2 = argv[1], argv[2]
    
    f1 = open(filenm1)
    f2 = open(filenm2)
    
    for i in range (159):
       l1 = f1.readline()
       l2 = f2.readline()
       if l1 != l2: 
          #if len(l1.split(', ')) != len(l2.split(', ')):
             print l1, '\t' + str(len(l1.split(', ')))
             print l2, '\t' + str(len(l2.split(', ')))
 
 
if __name__ == '__main__':
    main(sys.argv)
import sys




def comp_mono(f1, f2):
    # compares 67 line files in the same language line per line 
    for i in range (67):
       l1 = f1.readline()
       l2 = f2.readline()
       if l1 != l2: 
          #if len(l1.split(', ')) != len(l2.split(', ')):
             print l1, '\t' + str(len(l1.split(', ')))
             print l2, '\t' + str(len(l2.split(', ')))


def count_facts (f): 
     facts = {}
     for s in f: 
       s = s.strip()
       if s.isdigit():
          line_num = int(s) 
          if line_num not in facts: 
             facts[line_num] = 0 
          continue 
       if 'Arg1' in s or 'arg1' in s: 
          facts[line_num] +=1 
     print len(facts)     
     return facts     


def comp_bi(f1, f2):
    # compares numbers of facts per sentence inb files in different languages 
    facts_f1 = count_facts(f1)
    facts_f2 = count_facts(f2)
    
    i = 0 
    for line in facts_f1: 
      if facts_f1[line] != facts_f2[line]: 
         print "###########"
         print line 
         print 'f1 = ', facts_f1[line]
         print 'f2 = ', facts_f2[line]
         print facts_f1[line] - facts_f2[line]
         i +=1 
    print "differences: ", i



def main (argv):
    if len(argv) != 4:
        sys.stderr.write('Usage: %s option file1 file2 \n' % argv[0])
        sys.exit(-1)
    
    filenm1, filenm2 = argv[2], argv[3]
    opt = argv[1]
    
    OPTIONS = ['mono', 'bi']
    if opt not in OPTIONS: 
         sys.stderr.write('The only available options are "mono"  and "bi"' )
         sys.exit(-1)
           
    f1 = open(filenm1)
    f2 = open(filenm2)
    
    if opt == 'mono': 
       comp_mono(f1, f2)
    else: 
       comp_bi(f1, f2)    
    
    
    
 
 
if __name__ == '__main__':
    main(sys.argv)
import sys 
import re 
import functions
import regexps

# 
# FACT EXTRACTION WRAPPER
# USAGE: 
# $ python fact_extr_regexp.py  fact_extr.config  POS_tagged_file >STDOUT
#


##################################################################
#     FUNCTIONS
##################################################################
def process_config(configfn): 
    '''
    processes config file 
    '''
    config = open(configfn)
    params = [False for i in range(0, 6)]
    #print params 
    i = 0 
    for s in config: 
       if s.strip()[0] == '#': continue  # hash serves for comments 
          
       elif s.strip().split()[-1].strip() == '1':
          params[i] = True
       i += 1 
    print params    
    return  params 


#########################
#     MAIN 
#########################

def main (argv):
    if len(argv) != 3:
        sys.stderr.write('Usage: %s Config_file POS_tagged_file \n' % argv[0])
        sys.exit(-1)
    
    configfn, filenm = argv[1], argv[2]
         
    params = process_config(configfn)
    f = open(filenm)
    
    functions.find_facts_param(f, params)

 
if __name__ == '__main__':
    main(sys.argv)
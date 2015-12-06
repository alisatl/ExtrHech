import sys 
import re 
import functions
import regexps

# 
#
# USAGE: 
# $ python fact_extr_regexp.py  fact_extr.config  POS_tagged_file >STDOUT
#



###########################################################################
#                 REGULAR EXPRESSIONS 
###########################################################################


################
#   VERB PHRASE 
################

'''
V|VP|VW*P 

V = VERB PARTICLE? ADV?
W = (NOUN|ADJ|ADV|PRON|DET)
P = (PREP|PARTICLE|INF. MARKER)
'''


#V = r'(?:\w+\^\w+\^P0000000\s+)?(?:(?:\w+\^\w+\^V[M|S]I....)|(?:\w+\^\w+\^V[A|S]I....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?'

#takes into account dative case pronouns infront of a verb 
#V = 
V = r'(?:\w+\^\w+\^P[0|P].[0|C][0|P|S]000\s+)?(?:(?:\w+\^\w+\^V[M|S]I....)|(?:\w+\^\w+\^V[A|S]I....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?'

V_WITH_PARTICIP = r'(?:\w+\^\w+\^P[0|P].[0|C][0|P|S]000\s+)?(?:(?:\w+\^\w+\^V[M|S][IP]....)|(?:\w+\^\w+\^V[A|S]I....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?'


#W = r'(?:\s+(?:\w+\^\w+\^N......)|(?:\w+\^\w+\^A.....)|(?:\w+\^\w+\^R.)|(?:\w+\^\w+\^P.......)|(?:\w+\^\w+\^D.....)|(?:\w+\^\w+\^VMN....(?:\s+\w+\^\w+\^PP...000)?))'
W = r'(?:(?:\s+\w+\^\w+\^N......)|(?:\s+\w+\^\w+\^A.....)|(?:\s+\w+\^\w+\^R.)|(?:\s+\w+\^\w+\^P.......)|(?:\s+\w+\^\w+\^D.....)|(?:\s+\w+\^\w+\^VMN....(?:\s+\w+\^\w+\^PP...000)?))'
#W = r'(?:\s+(?:\w+\^\w+\^N......)|(?:\w+\^\w+\^A.....)|(?:\w+\^\w+\^R.)|(?:\w+\^\w+\^P.......)|(?:\w+\^\w+\^D.....))'





I = r'(?:\s+\w+\^\w+\^VMN....(?:\s+\w+\^\w+\^PP...000)?)'

#P = r'(?:\s+\w+\^\w+\^SP...)'
#P = r'(?:\s+\w+\^\w+\^SP...)|(?:\s+\w+\^\w+\^V.N....)'
#P = r'(?:(?:\s+\w+\^\w+\^SP...)|(?:\s+\w+\^\w+\^V.N....))'
P = r'(?:(?:\s+\w+\^\w+\^SP...\s+\w+\^\w+\^V.N....)|(?:\s+\w+\^\w+\^SP...)|(?:\s+\w+\^\w+\^V.N....))'

#REGEX_REL = '('+V+'(?:\s+'+W+')*'+P+')|('+V+P+')|('+V+')'   
#REGEX_REL = '('+V+ W+'*'+P+')|('+V+P+')|('+V+')'   
#REGEX_REL = '('+V+P+')|('+V+ W+'*'+P+')|('+V+')'   
VREL = '('+V+ W+'*'+P+')|('+V+')'   


# saca bien las relaciones verbales de 1-68 COMO SON EN CORPUS_HUMANO.XLS : 
#REGEX_REL = r'((?:\w+\^\w+\^P0000000)?\s+(?:(?:\w+\^\w+\^V[M|S]I....)|(?:\w+\^\w+\^VAI....\s+\w+\^\w+\^VMP....))(?:\s+\w+\^\w+\^RG)?(?:\s+(?:\w+\^\w+\^VMN....))*)'#\s+(?:\w+\^\w+\^SP...)?)'

###################
#     NOUN PHRASE 
###################

#noun with no participle clause 
#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?(?:\w+\^\w+\^N......)(?:\s+\w+\^\w+\^A.....)?'

#noun with a participle clause 
#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?(?:\w+\^\w+\^N......)(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?'

#noun or numeral 
#200^200^Z
NUM = r'(?:\d+\^\d+\^Z)'

# centuries 
# siglo_V_a.C.^[s:-v]^W (?:[\w\.]+\^\[.{3, 25}\]\^W)
SIG = r'(?:[\w\.]+\^\[.{3,25}\]\^W)'

#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?(?:(?:\w+\^\w+\^N......)|(?:\d+\^\d+\^Z))(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?'
#N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?(?:\d+\^\d+\^Z)?(?:(?:\w+\^\w+\^N......)|(?:\d+\^\d+\^Z))(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?'

N = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?'+NUM+'?(?:(?:\w+\^\w+\^N......)|'+NUM+'|'+SIG+')(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?'


# this regex works very badly for spanish 
N_WITH_PRONOUN =  r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^A.....\s+)?'+NUM+'?(?:(?:\w+\^\w+\^N......)|(?:\w+\^\w+\^PP......)|'+NUM+'|'+SIG+')(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^VMP....)?'

PREP = r'(?:\s+\w+\^\w+\^SP...\s+'+N+')' 

#PARTICIP = r'(?:\s+\w+\^\w+\^VMP....\s+\w+\^\w+\^SP...\s+'+N+')' 
PARTICIP = r'(?:\s+\w+\^\w+\^VMP....\s+\w+\^\w+\^SP...\s+'+N+PREP+'?)' 

#NP = r'(?:\w+\^\w+\^D[^TE]....\s+)?(?:\w+\^\w+\^N......)(?:\s+\w+\^\w+\^A.....)?(?:\s+\w+\^\w+\^SP...\s+'+N+')?' 
#NP = N+r'(?:\s+\w+\^\w+\^SP...\s+'+N+')?' 
NP = N+'(?:'+PREP+'|'+PARTICIP+')?'


#########################################
#   RELATIVE PRONOUNS (que, cual, quien)
#########################################

QUE = r'(?:\s+\w+\^\w+\^PR0C....)'



###################################################################


def count_rels(arr): 
    cnt = 0 
    if isinstance(arr[0], tuple): 
        for tulp in arr: 
          for el in tulp: 
           if el != '': 
              cnt +=1
    else: 
        cnt = len(arr)          
    return cnt           
          

def find_iter_for_file(file, pat):
    matches = []
    i = 1
    j = 0 
    c = 0 
    for s in file: 
      matches = pat.finditer(s)
      if matches == None: 
         print i , 'No matches found' 
         j+=1
      else: 
         for m in matches: 
           print i, m.group(), m.start(), m.end(), m.span()  
           c +=1  
      i+=1 

    print "Total of ", c, "relation phrases found"
    print "Total of ", j, "sentences without matches"
    return c, j
    

def find_pattern_for_file(file, regex):
    '''
    finds all pattern matches in a files 
    '''
   
    pat = re.compile(regex, re.I|re.U)
    founds = []
    i = 1
    j = 0 
    c = 0 
    
    for s in file: 
      founds = pat.findall(s)
      if founds == []: 
         print i , 'No matches found' 
         j+=1
      else: 
         print i, founds  
         c +=count_rels(founds)   
      i+=1 

    print "Total of ", c, "noun phrases found"
    print "Total of ", j, "sentences without matches"
    
    return c, j 


def find_facts(file, vp_re, np_re):
    vp_pat = re.compile(vp_re, re.I|re.U)
    np_pat = re.compile(np_re, re.I|re.U) 
    
    facts = 0
    matches = []
    i = 1
    j = 0 
    c = 0 
    f = 0 
    
    #verb_phrases = []
        
    for s in file: 
      verbs = vp_pat.finditer(s)
      
      if verbs == None:
         facts.append(str(i)+' No matches for verb phrase found')
         print i , 'No matches for verb phrase found' 
         j+=1
      else:
         new_start = 0      
         for v in verbs:
           #print i, v.group(), v.start(), v.end(), v.span()  
           nouns_left = np_pat.finditer(s, new_start, v.start())
           #if i ==11: 
           #   print nouns_left.group() 
           
           if nouns_left == None: 
              print i, '\t No matches for left argument'
           else:  
              noun_right = np_pat.search(s, v.end())
              if  noun_right == None:
                  print i, '\t No matches for right argument'
              else: 
                  arg1 = None 
                  for n in nouns_left: pass
                  #arg1 = nouns_left[-1].group()
                  arg1 = n.group()
                  if n.end()+1 == v.start(): 
                      print i
                      print '\t arg1 = ', arg1, n.end(), "New start = ",  new_start
                      print '\t Rel = ', v.group(), v.start(), v.end()
                      print '\t arg2 = ', noun_right.group(), noun_right.start(), noun_right.end()        
                      new_start =  noun_right.end() 
                      f += 1
                      nouns_left = None
                  else: 
                      print i, "\t The end of Arg1 and Rel_Phrase are not the same" 
           c +=1  
      i+=1 

    print "Total of ", f, "facts found"
    print "Total of ", c, "relation phrases found"
    print "Total of ", j, "sentences without matches"
    return f, j


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


####################
#     MAIN 
####################

def main (argv):
    if len(argv) != 3:
        sys.stderr.write('Usage: %s Config_file POS_tagged_file \n' % argv[0])
        sys.exit(-1)
    
    configfn, filenm = argv[1], argv[2]
         
    params = process_config(configfn)
    f = open(filenm)
    
    
    #find_pattern_for_file(f, regexps.VREL) 
    #find_facts(f, VREL, NP)
    functions.find_facts_param(f, params)

 
if __name__ == '__main__':
    main(sys.argv)
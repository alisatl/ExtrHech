import re 
import regexps
import sys 

CORPUS = 'D:/Study/OpenInfoExtraction/corpus/knowfact_corpus_v4.txt'


def print_out(i, ng1, v, ng2, new_start): 
    # custom PRINT function 
    print i
    print 'arg1 = ', cut_wordforms(ng1.group())#, ng1.end(), "New start = ",  new_start
    print 'Rel = ', cut_wordforms(v.group())#, v.start(), v.end()
    print 'arg2 = ', cut_wordforms(ng2.group())#, ng2.start(), ng2.end()
    return True  


def print_out_prep(i, ng1_group, v_group, ng2_group): 
    # custom PRINT function 
    print i
    print 'arg1 = ', cut_wordforms(ng1_group)
    print 'Rel = ', cut_wordforms(v_group)
    print 'arg2 = ', cut_wordforms(ng2_group)
    return True


def print_out_right_arr(i, ng1, v, args2, new_start):
    # custom PRINT function  for an array of right arguments 
    print i
    for arg2 in args2:
         print 'Arg1 = ', cut_wordforms(ng1.group())#, ng1.end(), "New start = ",  new_start
         print 'Rel = ', cut_wordforms(v.group())#, v.start(), v.end()
         print 'Arg2 = ', cut_wordforms(arg2.group())#, arg2.start(), arg2.end(), '\n'
    return True

def print_out_right_arr_prep(i, args1, v, ng2_group, new_start):
    print i
    for arg in args1:
         print 'Arg1 = ', cut_wordforms(arg.group())
         print 'Rel = ', cut_wordforms(v.group())
         print 'Arg2 = ', cut_wordforms(ng2_group)
    return True



def cut_wordforms (group): 
      #cuts the original wordfroms from a phrase of POS-tagged words 
      words = group.split()
      phrase = ''
      for w in words: 
          phrase += w[:w.find('^')] + ' '
      return phrase 
      

def read_corpus(fnm):
    corpus = []
    fcorpus = open(fnm)
    for s in fcorpus: 
       corpus.append(s.strip())
    fcorpus.close()
    return corpus   


def detect_prev_word(ng1, s):
    if ng1.start() == 0: 
      #print 'No previous word'
      return None 
    else:
      w = s[:ng1.start()-1].split()[-1] 
      #print 'Previous word is ', w
      w_spl = w.split('^')
      if w_spl[-1][0] == 'S':
          #print 'Previous word is a preposition'     
          return w+' '
      else: 
          #print 'Previous word is NOT a preposition'
          return None    

#===========================================================

'''
def find_facts2(file, vp_re, np_re):
    # This function does not check the distance between Arg1 and Verb phrase 
    vp_pat = re.compile(vp_re, re.I|re.U)
    np_pat = re.compile(np_re, re.I|re.U) 
        
    i = 1
    j = 0 
    c = 0 
    f = 0 
    
            
    for s in file: 
      print '###############'
      verbs_iters = vp_pat.finditer(s)
      verbs = list(verbs_iters)      
            
      if verbs == []:
         print i , 'No matches for verb phrase found' 
         j+=1
      else:
         new_start = 0 
         for v in verbs:
           nouns_left_iters = np_pat.finditer(s, new_start, v.start())
           nouns_left = list(nouns_left_iters)
           
           if nouns_left == []: 
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
                  #if n.end()+1 == v.start(): 
                  print i
                  print 'arg1 = ', cut_wordforms(arg1), n.end(), "New start = ",  new_start
                  print 'Rel = ', cut_wordforms(v.group()), v.start(), v.end()
                  print 'arg2 = ', cut_wordforms(noun_right.group()), noun_right.start(), noun_right.end()        
                  new_start =  v.end() 
                  f += 1
                  nouns_left = None
                  #else: 
                  #    print i, "\t The end of Arg1 and Rel_Phrase are not the same" 
           c +=1  
      i+=1 

    print "Total of ", f, "facts found"
    print "Total of ", c, "relation phrases found"
    print "Total of ", j, "sentences without matches"
    return f, j
   
    
#=====================================================    

def find_facts_rel(file, vp_re, np_re, que_re):
    # This function takes in account relative clauses 
    vp_pat = re.compile(vp_re, re.I|re.U)
    np_pat = re.compile(np_re, re.I|re.U) 
    que_pat = re.compile(que_re, re.I|re.U)
        
    i = 1
    j = 0 
    c = 0 
    f = 0 
        
    
    for s in file: 
      print '###############'
      verbs_iters = vp_pat.finditer(s)
      verbs = list(verbs_iters)
      no_fact = True       
            
      if verbs == []:
         print i
         print 'No matches for verb phrase found' 
      else:
         new_start = 0 
         for v in verbs:
           nouns_left_iters = np_pat.finditer(s, new_start, v.start())
           nouns_left = list(nouns_left_iters)
           
           if nouns_left == []: 
              print i
              print '\t No matches for left argument'
           else:  
              noun_right = np_pat.search(s, v.end())
              if  noun_right == None:
                  print i
                  print '\t No matches for right argument'
              else: 
                  #arg1 = None 
                  #for n in nouns_left: pass
                  ng1 = nouns_left[-1]
                  #arg1 = ng1.group()
                  #arg1 = n.group()
                  if ng1.end()+1 != v.start():
                     if que_pat.search(s, ng1.end(), v.start()) == None: 
                        print i 
                        print 'Arg 1 and Verb Phrase are apart and not connected by relative pronoun'
                     else: 
                        no_fact = print_out(i, ng1, v, noun_right, new_start)
                        f += 1   
                  else:       
                     no_fact = print_out(i, ng1, v, noun_right, new_start)
                     
                     
                    # print i
                    # print 'arg1 = ', cut_wordforms(arg1), ng1.end(), "New start = ",  new_start
                    # print 'Rel = ', cut_wordforms(v.group()), v.start(), v.end()
                    # print 'arg2 = ', cut_wordforms(noun_right.group()), noun_right.start(), noun_right.end()
                     
                     f += 1        
                  new_start =  v.end() 
                  
                  #else: 
                  #    print i, "\t The end of Arg1 and Rel_Phrase are not the same" 
           c +=1  
      i+=1 
      if no_fact: j+=1

    print "Total of ", f, "facts found"
    print "Total of ", c, "relation phrases found"
    print "Total of ", j, "sentences without facts"
    return f, j
 '''   
# ======================================================

'''
Params  (default)
0) RELATIVE_CLAUSE = 1
1) PARTICIPLES = 1
2) PRONOUNS = 1
3) COORD_CONJ_VERB = 0
4) COORD_CONJ_NOUN = 0 
5) IGNORE_DISTANCE = 0
'''


def find_facts_param (file, params):
    '''
     This function takes in an array of config params and compiles regexps from regexps.py  
    ''' 
    # redaing original sentences from a file  
    corpus = read_corpus(CORPUS)
    
    verb_coord = False  
    
    if params[0]: 
       # if relative clauses as facts 
       que_pat = re.compile(regexps.QUE, re.I|re.U)
       #for cases like: '70 La barbarie, la perdida, inspiraron estos once pequenos cuadros.'
       comma_pat = re.compile(regexps.COMMA, re.I|re.U)
    
    if params[1]: 
      # if participles as facts 
      V = regexps.V_WITH_PARTICIP
      vp_re = '('+V+ regexps.W+'*'+regexps.P+')|('+V+')'   
    else: 
      vp_re = regexps.VREL
      
    if params[2]:
      # if considering pronouns as arguments  
      N = regexps.N_WITH_PRONOUN    
      np_re = N+'(?:'+regexps.PREP+'|'+regexps.PARTICIP+')?'  
    else: 
      np_re = regexps.NP 
    
    if params[3]:
       verb_coord = True 
       coord_pat  = re.compile(regexps.COORD, re.I|re.U)
       
    if params[4]:
       #if coordinate conjunctions for NOUNs as independent arguments 
       coord_pat  = re.compile(regexps.COORD, re.I|re.U)
       
     
        
    
    vp_pat = re.compile(vp_re, re.I|re.U)
    np_pat = re.compile(np_re, re.I|re.U) 
    
        
    i = 1   # line counter 
    j = 0   # fact counter 
    c = 0   # counter for relation phrases 
    f = 0   # counter of sentences with no facts 
        
    no_left_match = False
    
    fcorpus = open(CORPUS)
    
    for s in file: 
      verbs_coord_direct = False 
      verbs_coord_indirect = False 
      second_verbs = {}
      first_verbs = {}
      
      print '###############'
      print  fcorpus.readline()
            
      
      #########################
      #####checking verbs###### 
      #########################
      verbs_iters = vp_pat.finditer(s)
      verbs = list(verbs_iters)
      got_fact = False       
            
      if verbs == []:
         print i
         print 'No matches for verb phrase found' 
      else:
         new_start = 0 
         #for v in verbs:
         for cnt in range(len(verbs)):
           v = verbs[cnt] 
           if params[1]:  
              # if current verb is a participle and it's adjacent to a verb, skip 
              if re.search('V[M|S]P', v.group()) != None and cnt != len(verbs)-1 and v.end()+1 == verbs[cnt+1].start(): continue 
           
           if verb_coord and cnt < len(verbs)-1: 
              # if we are considering conjuntcive coordination of verbs ...
              coord = coord_pat.search(s, v.end(), verbs[cnt+1].start())
              # check if the conjunction is adjacent to the left of the next verb  
              if coord != None and coord.end()+1 == verbs[cnt+1].start():
                 if v.end() == coord.start():
                    #verbs_coord_direct  
                    second_verbs[verbs[cnt+1]] = 0
                    first_verbs[v] = 0       
                 else: 
                    #verbs_coord_indirect = True
                    second_verbs[verbs[cnt+1]] = 1
                    first_verbs[v] = 1       
           
           ####################################
           ######checking left argument########
           ####################################                              
           if v in second_verbs and second_verbs[v] == 1 and not no_left_match:
              # if it's a verb in a second position like " es la prolongacion del encefalo, TIENE FORMA DE cordon... "
              pass 

           else: 
              # setting flags
              no_left_match = False
              prep_flag = False 
               
              nouns_left_iters = np_pat.finditer(s, new_start, v.start())
              nouns_left = list(nouns_left_iters)
                      
              if nouns_left == []: 
                 print i
                 print '\t No matches for left argument'
                 no_left_match = True 
              else:    
                 ng1 = nouns_left[-1]
                 
                 #####################################
                 ####checking previous preposition####
                 #####################################
                 
                 w_prev = detect_prev_word(ng1, s)
                 if w_prev: 
                   prep_flag = True 
                 
                 if ng1.end()+1 != v.start():
                   if params[0]:   # if we're considering relative clauses
                      #if que_pat.search(s, ng1.end(), v.start()) == None:
                      if que_pat.search(s, ng1.end(), v.start()) == None or comma_pat.search(s, ng1.end(), v.start()) == None:
                          print i 
                          print ng1.end(), v.start()
                          print 'Arg 1 and Verb Phrase are apart and not connected by relative pronoun'
                          no_left_match = True
                   else: 
                     print i 
                     print 'Arg 1 and Verb Phrase are apart'
                     no_left_match = True
                            
           #####################################
           ########checking right argument######
           #####################################                              
           arg2_start_pos_changed = False 
           if v in first_verbs and first_verbs[v] == 0:
              arg2_start_pos_changed = True 
           
           if not no_left_match:
              no_right_match = False
              
              '''
              if arg2_start_pos_changed: 
                 arg2_start_pos = verbs[cnt+1].end()
              else:    
                 arg2_start_pos = v.end()
              ''' 
              
                 
              if params[4]:
                 if cnt != len(verbs)-1: 
                 # if we're not  in the last verb cycle 
                    nouns_right_iters = np_pat.finditer(s, v.end(), verbs[cnt+1].start())
                 else:    
                    nouns_right_iters = np_pat.finditer(s, v.end())
                 nouns_right = list(nouns_right_iters)
                 if nouns_right == []: 
                    print i
                    print '\t No matches for right argument'
                    no_right_match = True 
                 else: 
                    args2 = [nouns_right[0]]
                    if len(nouns_right) > 1:    
                      for cnt2 in range(len(nouns_right)-1):
                         # if right noun groups are connected by a coordinative conjunction or comma 
                         not_adjacent = True 
                         coord = coord_pat.match(s, nouns_right[cnt2].end(), nouns_right[cnt2+1].start())
                         if coord != None:
                            #print i
                            #print  nouns_right[cnt2].end(), coord.start(), coord.end()+1, nouns_right[cnt2+1].start()
                            if nouns_right[cnt2].end() == coord.start() and  coord.end()+1 == nouns_right[cnt2+1].start():
                               args2.append(nouns_right[cnt2+1])
                               not_adjacent = False 
                               
                         if not_adjacent:  break       

              else:  
                noun_right = np_pat.search(s, v.end())
                if  noun_right == None:
                    print i
                    print '\t No matches for right argument'
                    no_right_match = True
                
              if not no_right_match: 
                    if params[4]:  
                        if prep_flag:
                          # adding the preposition to ng1 and swapping ng1 and ng2
                          ng2_group = (w_prev) + ng1.group()
                          got_fact = print_out_right_arr_prep(i, args2, v, ng2_group, new_start)
                        else:  
                          got_fact = print_out_right_arr(i, ng1, v, args2, new_start)
                        f+=len(args2)
                    else:
                        if prep_flag:
                          # adding the preposition to ng1 and swapping ng1 and ng2
                          ng2_group = (w_prev) + ng1.group()
                          ng1_group = noun_right.group()
                          v_group = v.group()
                          got_fact = print_out_prep(i, ng1_group, v_group, ng2_group)  
                        else:   
                          got_fact = print_out(i, ng1, v, noun_right, new_start)
                        f += 1      
                    new_start =  v.end() 
                  
           c +=1  
      i+=1 
      if not got_fact: j+=1

    print "\n"
    print "Total of ", f, "facts found"
    print "Total of ", c, "relation phrases found"
    print "Total of ", j, "sentences without facts"
    return f, j






    
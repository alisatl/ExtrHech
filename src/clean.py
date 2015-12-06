fout = open('knowfact_corpus_v4_clean.txt', 'w')
for s in open('knowfact_corpus_v4.txt'):
  print >>fout, s.strip()

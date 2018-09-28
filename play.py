import pythag

p = pythag.Pythag()

for i in range(1, 11, 2):
  triples = p.calc_triples(i*i)

  print "Triples for %d:" % (i*i)

  for t in triples:
    print t

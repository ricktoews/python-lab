import pythag

def get_pythag():
  p = pythag.Pythag()
  corners = [1, 2, 9, 25]
  result = []

  for i in corners:
    triples = p.calc_triples(i)

    result.append({ "corner": i, "triples": triples })

    #for t in triples:
    #  result.append(t)

  return result

print get_pythag()



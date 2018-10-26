import pythag

def get_pythag():
  p = pythag.Pythag()
  corners = [1, 2, 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529, 625, 729, 841, 961, 1089, 1225, 1369, 1521, 1681, 1849, 2025]
  result = []

  for i in corners:
    triples = p.calc_triples(i)

    result.append({ "corner": i, "triples": triples })

    #for t in triples:
    #  result.append(t)

  return result

print get_pythag()



import math

class Pythag:
  corner = 1

  def find_alternatives(self, triple):
    diff = []
    squares = []
    (a, b, c) = triple
    upper_limit = int(c - 1)
    for n in range(1, upper_limit):
      squares.append(n*n)

    for s in squares:
      check = c*c - s
      sqrt = math.sqrt(check)
      if (sqrt != a and sqrt != b and int(sqrt) == sqrt):
        diff.append(int(sqrt))

    return diff


  def set_corner(self, n):
    self.corner = n*n


  def get_squares(self):
    squares = []
    sqrt = math.sqrt(self.corner)
    for i in range(1, 10):
      sqrt += 2
      squares.append(sqrt*sqrt)
    return squares


  def calc_triples(self, c = 1):
    triple = []
    self.set_corner(c)
    squares = self.get_squares()
    for sq in squares:
      a = int((sq - self.corner) / 2)
      b = int(math.sqrt(self.corner * self.corner + 2*self.corner*a))
      c = int(math.sqrt(a*a + b*b))
      t = [a, b, c]
      alts = self.find_alternatives(t)
      t.sort()
      t.append(alts)
      triple.append(t)

    return triple

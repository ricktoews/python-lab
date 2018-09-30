import math

class Pythag:
  corner_side = 1

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


  def set_corner_side(self, n):
    """ The corner here is the upper left corner of c^2. It's the corner of the wrap formed by b^2. """
    self.corner_side = n


  def get_odd_squares(self):
    """ I think these are candidates for n + 2a, which must be an odd square. """
    squares = []
    side = math.sqrt(self.corner_side)
    for i in range(1, 5):
      side += 2
      squares.append(side*side)
    return squares

  def calc_triples(self, c = 1):
    """ 
    We're going specifically for primitive triples. 
    Imagine a square grid of unit squares. This is a^2.
    Now, imagine wrapping squares around the top and one of the sides.
    These squares are b^2, but they're arranged as a corner shape: a vertex and two perpendicular legs.
    This gives us a larger square, which is c^2.
    Let n be the difference between one c and a. So n^2 is the square that at the juncture of the
    shape that b^2 takes as a wrapper for a^2.
    Thus, b^2 can be expressed as n^2 + 2*a*n, or n(n+2a).
    A primitive triple is one that doesn't have any common factors.
    For b^2 and a^2 to not share any factors, n must meet one of two conditions:
    n must be an odd square, or n must equal 2.
    Given that n is square, n+2a will also be square, and we can find candidate values.
    We will find these values by squaring every each odd number after n.
    """
    triple = []
    self.set_corner_side(c)
    squares = self.get_odd_squares()
    for sq in squares:
      # with sq = n + 2a, solve for a.
      a = int((sq - self.corner_side) / 2)
      # b^2 is n^2 + 2an. Take the square root of that.
      b = int(math.sqrt(self.corner_side * self.corner_side + 2*(self.corner_side)*a))
      c = int(math.sqrt(a*a + b*b))
      t = [a, b, c]
      alts = self.find_alternatives(t)
      t.sort()
      #t.append(alts)
      triple.append(t)

    return triple

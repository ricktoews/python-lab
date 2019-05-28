import math

"""
This class was designed to calculate Pythagorean Triples; and, specifically, primitives.
A primitive is one in which 1 is the greatest common factor of a, b, and c.
The concept is to view c^2 as a square grid of unit squares, containing a^2 in the lower
right corner, with a^2 wrapped by b^2. In this way, b^2 consists of two rectangles of
area 2*a and a corner square of area (c-a)^2.

For convenience, let n = c - a. Thus, 
b^2 = n^2 + 2*a*n. 

For present purposes, it will be convenient to factor out the n; so, 
b^2 = n(n + 2a).

In order for n(n + 2a) to be square, either n must itself be square, or (n + 2a) must be
a multiple of n. If (n + 2a) is a multiple of n, then 2a is a multiple of n, and either
n == 2, or n and a are not relatively prime.

Let's consider the case of n being square. Specifically, n must be an odd square. Here's why:
n + 2a can easily be a square and have 1 as GCF of a and n.
If n is an even square, then n's factors include 2 raised to an even power. Because 2a
has only 2^1 besides a, an even power of 2 would require a to be even and thus, because n
woudl also be even, the GCF of a and n would be greater than 1.

I. So if n is a square, it must be an odd square.

To find values of n(n + 2a) that are square:
  Start with n as an odd square.
  Find a square that can be expressed as (n + 2a). This is done by taking the
  square root of n, adding a multiple of 2, and squaring the sum.
  Multiply the result by n, giving n(n + 2a), or b^2.
  Example: n = 9.
  Square root of 9 is 3.
  Adding multiples of 2 to 3, we get 5, 7, 9, 11, &c.
  Squaring these: 25, 49, 81, 121, &c.
  Multiplying these by 9: 225, 441, 729, 1089, &c.

To find a, we subtract n from (n + 2a), and then divide by 2.
  Example, continuing with n = 9:
  For (n + 2a) = 25, a = 8: (25 - 9) / 2
  For (n + 2a) = 49, a = 20: (49 - 9) / 2
  For (n + 2a) = 81, a = 36: (81 - 9) / 2

To get b, we take the square root of n(n + 2a).
  For n(n + 2a), with n = 9:
  For a = 8: 9(9 + 16) = 225; square root is 15
  For a = 20: 9(9 + 40) = 441; square root is 21
  For a = 36: 9(9 + 72) = 729; square root is 27

To get c, (a^2 + b^2), and take the square root.
  

II. The other possibility is that n = 2.

This is actually a little more straightforward, since n(n + 2a) is much more constrained.
2(2 + 2a) = 4 + 4a = 4(1 + a), which is an even square.

Since 1 + a is a square, and the GCF of a and n must be 1, a is (2x)^2 - 1, where x is
an integer. The values for a are 3, 15, 35, 63, &c.

For a given value of a, b^2 = 4 + 4*a, and b is the square root.
Example: a = 3; b^2 = 16, so b = 4. We find c in the usual way: sqrt(9 + 16); so (3, 4, 5)
Another: a = 15; b^2 = 64, so b = 8. sqrt(64 + 225); so (8, 15, 17)
&c.

"""
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
    """ 
    The corner here is the upper left corner of c^2. It's the corner of the wrap formed by b^2. 
    The b^2 is n^2 + 2na, which is also n(n + 2a). For Pythagoren Triples that are primitives, 
    n must be either 2 or the square of an odd number.
    """
    self.corner_side = n


  def get_odd_squares(self):
    """ 
    These are candidates for n + 2a, which must be an odd square. 
    Example: For n == 9, the squares are 25, 49, 81, 121, &c.
    """
    squares = []
    side = math.sqrt(self.corner_side)
    for i in range(1, 50):
      side += 2
      squares.append(side*side)
    return squares

  def get_even_squares(self):
    """
    When the corner side is 2, b^2 == n^2 + 2an == 4 + 4a == 4(1+a).
    The even squares, then, are simply 4, 16, 36, 64, &c.
    """
    squares = [4*x*x for x in range(1, 50)]
    return squares

  def calc_a_b_c(self, sq):
    """
    There are two different situations to accommodate in calculating a and b.
    For triples with an odd square as the difference between c and a:
      b^2 is n^2 + 2an, or n(n + 2a). n is the corner side, or the square root
      of the area of the corner square. The area of b^2 is the corner square plus
      the two sides overlapping a^2. The corner square is n^2, and the area of
      each overlap side is a*n. 
    """
    if self.corner_side % 2 == 0:
      a = sq - 1
      b = int(math.sqrt(4 + 4 * a))
    else:
      # with sq = n + 2a, solve for a.
      a = int((sq - self.corner_side) / 2)
      # b^2 is n^2 + 2an. Take the square root of that.
      b = int(math.sqrt(self.corner_side * self.corner_side + 2*(self.corner_side)*a))

    c = int(math.sqrt(a*a + b*b))
    if self.corner_side > 1 and a % self.corner_side == 0:
      a = b = c = 0

    return [a, b, c]

  def calc_triples(self, side = 1):
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
    self.set_corner_side(side)
    if side % 2 == 0:
      squares = self.get_even_squares()
    else:
      squares = self.get_odd_squares()
    #print "calc_triples corner {side}, squares {squares}".format(side=side, squares=squares)
    stop = False;
    for sq in squares:
      [a, b, c] = self.calc_a_b_c(sq)

      if a != b:
        t = [a, b, c]
        alts = self.find_alternatives(t)
        t.sort()
        #t.append(alts)
        if not stop:
          t_str = ', '.join(map(lambda x: str(x), t))
          t_str = t_str + '; diff ' + str(b-a)
          triple.append(t_str)

        stop = b - a < 0

    return triple

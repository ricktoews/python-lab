import math
from pascal_triangle import PT

SQRT_5 = math.sqrt(5)
PHI = (1 + SQRT_5) / 2

def apply_pascal(n):
  """ Apply the Pascal Triangle to sqrt(5) + 1 to get the denominator for the requested power of phi. """
  coefs = PT[n]
  _p = n
  root = 0
  whole = 0
  for _c in coefs:
    if _p % 2 == 0:
      whole += _c * 5**(_p / 2)
    else:
      root += _c * 5**((_p - 1) / 2)
    _p -= 1

  result = { "whole": whole, "root": root }
  return result


def reduce_fraction(whole_root5, n):
  """ Because we want the fraction denominator to be 2, we must divide out 2^(n-1). """
  _reduce = 2 ** (n - 1)
  whole_root5['whole'] /= _reduce
  whole_root5['root'] /= _reduce

  return whole_root5


def power_of_phi(n):

  whole_root5 = apply_pascal(n)
  phi = reduce_fraction(whole_root5, n)

  return phi


def phi_powers(n):
  """Calculate the first n phi powers"""
  powers = []
  for _ in range(1, n+1):
    powers.append({ "power": _, "phi": power_of_phi(_) })

  return powers

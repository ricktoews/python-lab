import math

# get_corners returns an array of odd squares: 1, 9, 25, &c.
def get_corners():
  corners = []
  for i in range(1, 5002, 2):
    corners.append(i*i)

  corners.sort()
  return corners


# calc_a_b returns the a and b elements of a triple, given a corner value.
def calc_a_b(corner):
  last_corner = corner
  while True:
    sr = math.sqrt(last_corner)
    next_sq = (sr + 2) * (sr + 2)
    a = (next_sq - corner) / 2
    b_2 = corner*corner + 2 * corner * a
    b = math.sqrt(b_2)
    last_corner = next_sq
    result = [a, b]
    yield result

# diff_1_search accepts a corner value and looks for a and b values with a difference of 1.
def diff_1_search(corner):
  a = b = c = 0
  safety = 0
  search_result = { 'found': False }
  if corner % 2 == 1:
    done = False
    calc = calc_a_b(corner)
    found = False
    while not done:
      safety += 1
      [a, b] = next(calc)
      triple = [a, b, math.sqrt(a*a+b*b)]
      triple = map(lambda x: int(x), triple)
      triple.sort()
      if triple[1] - triple[0] == 1:
        search_result = { 'triple': triple, 'corner': corner, 'step': safety }
        found = True;

      if b - a < 0 or safety > 10000:
        done = True

  search_result['found'] = found
  return search_result


corners = get_corners()
for c in corners:
  search = diff_1_search(c)
  if search['found']:
    print search

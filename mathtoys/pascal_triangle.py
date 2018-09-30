def _build_triangle(tiers=50):
  """ Build the Pascal Triangle, to the specified number of tiers. """
  _tiers = [[1], [1, 1]]
  _t = 2
  while _t <= tiers:
    _tier = []
    _to_left = 0
    _last = _tiers[_t - 1]
    for _i in _last:
      _tier.append(_to_left + _i)
      _to_left = _i
    _tier.append(1)
    
    _tiers.append(_tier)
    _t += 1

  return _tiers

PT = _build_triangle()

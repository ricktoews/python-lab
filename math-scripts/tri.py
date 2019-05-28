def math_decorator(fn):
  def new_fn(*args, **kwargs):
    output = []
    output.append("Decoration before function.")
    output.append(fn(*args, **kwargs))
    output.append("Decoration after function.")

    return output

  return new_fn


@math_decorator
def tri(n):
  return n*(n+1)/2


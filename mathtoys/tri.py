import click

@click.command()
@click.argument('nth')
def nth_tri(nth):
  """ Return the nth triangular number. """
  n = int(nth)
  _tri = n * (n+1) / 2
  click.echo(_tri)

if __name__ == '__main__':
  nth_tri()

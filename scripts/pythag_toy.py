import click

@click.command()
@click.option("--starting", prompt="Starting c value", help="Example: 5, for the triple (3, 4, 5).")
@click.option("--ending", prompt="Ending c value", help="Within reason.")
@click.option("--focus", prompt="Focus (All, Primes)", help="")
def pythag_setup(starting, ending, focus):
    """Fire up a pythag triples toy."""
    count = int(count)
    for _ in range(count):
        click.echo("Hello, %s!" % name)

if __name__ == '__main__':
    hello()

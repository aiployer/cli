import click

from aiployer_parser import main

@click.command()
@click.argument('arg')
def cli(arg):
    main(arg)

if __name__ == '__main__':
    cli()

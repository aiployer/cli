import click

from aiployer_parser import main

@click.command()
@click.argument('arg')
def cli(arg):
    mapping = main(arg)
    click.echo(f'Mapping: {mapping}')

if __name__ == '__main__':
    cli()

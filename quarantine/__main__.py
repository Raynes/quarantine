import click
from quarantine.cdc import CDC


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
@click.argument('pip_args', nargs=-1)
def install(name, pip_args):
    """Install the package. Pip args specified with --."""
    cdc = CDC(name)
    cdc.install(pip_args)

@cli.command()
@click.argument('name')
def uninstall(name):
    """Uninstall the package, environment and all."""
    cdc = CDC(name)
    cdc.uninstall()

if __name__ == '__main__':
    quarantine()

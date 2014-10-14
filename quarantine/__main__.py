import click
from pycolorterm.pycolorterm import print_pretty
from quarantine.cdc import CDC
from sh import ErrorReturnCode


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
@click.argument('pip_args', nargs=-1)
def install(name, pip_args):
    """Install the package. Pip args specified with --."""
    cdc = CDC(name)
    try:
        cdc.install(pip_args)
    except ErrorReturnCode as e:
        print_pretty("<FG_RED>Something went wrong! Rolling back...<END>")
        cdc.uninstall()

@cli.command()
@click.argument('name')
def uninstall(name):
    """Uninstall the package, environment and all."""
    cdc = CDC(name)
    cdc.uninstall()

if __name__ == '__main__':
    quarantine()

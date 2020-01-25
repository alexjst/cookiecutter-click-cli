import click

@click.group()
def cli():
    """
    {{ cookiecutter.description }}
    """
    pass

@cli.command()
def version():
    """
    Print the version and exit
    """
    click.echo("{{ cookiecutter.version }}")

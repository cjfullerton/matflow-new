import logging
import click

from matflow import MatFlow
import matflow.api

logger = logging.getLogger(__name__)
cli = MatFlow.CLI


@cli.group()
def parameter():  # matflow-only command group
    pass


@parameter.command("search")  # matflow-only command
def parameter_search():
    matflow.api.parameter_search()


if __name__ == "__main__":
    cli()

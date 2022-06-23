import click

from . import prom


@click.group(help="Python Prometheus Client")
def cli():
    pass


# TODO - replace types with datetime objects
@cli.command()
@click.argument(
    "metric",
    type=str,
    # required=True,
    # help="Name of the metric to be queried",
)
@click.option(
    "-s",
    "--start",
    type=str,
    default="2022-06-21T00:00:00.000Z",
    show_default=True,
    help="Start time of the query in your local time",
)
@click.option(
    "-e",
    "--end",
    type=str,
    default="2022-06-22T06:00:00.000Z",
    show_default=True,
    help="End time of the query in your local time",
)
@click.option(
    "-t",
    "--time-step",
    type=int,
    default=15,
    show_default=True,
    help="Time interval between measurements in seconds",
)
@click.option(
    "--plot",
    is_flag=True,
    help="Optionally plot the queried metrics",
)
@click.option(
    "--dump",
    is_flag=True,
    help="Optionally dump the queried metrics to stdout",
)
def query(metric: str, start: str, end: str, time_step: int, plot: bool, dump: bool):
    """Query METRIC from the Prometheus database."""
    try:
        metrics: list[prom.Metric] = prom.query(metric, start, end, time_step)
    except prom.ResponseException as e:
        click.secho(f"{type(e).__name__}: {e}", fg="red")
        exit(1)
    else:
        if dump:
            # TODO Fix typing error
            for metric in metrics:  # type: ignore
                click.secho(f"\n{str(metric)}")

        if plot:
            prom.plot(metrics)

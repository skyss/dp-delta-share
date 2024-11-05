import click
import delta_sharing
import pandas as pd

pd.options.plotting.backend = "plotly"

client = delta_sharing.SharingClient("config.share")


@click.group(chain=True)
def cli() -> None:
    """Tool for downloading or plotting data from Skyss share."""


@cli.command()
def list_tables() -> None:
    tables = client.list_all_tables()
    for table in tables:
        print(f"{table.share}.{table.schema}.{table.name}")


@cli.command()
@click.argument("table", nargs=1)
@click.argument("group", nargs=1)
def plot_table(table: str, group: str) -> None:
    df = delta_sharing.load_as_pandas(f"config.share#{table}")
    df.groupby([df.timestamp.dt.date, group]).size().unstack(1).plot(
        kind="bar", log_y=True, title=f"Log plot grouped by {group}"
    ).show()


@cli.command()
@click.argument("table", nargs=1)
@click.option("-o", "--output", default="csv", help="Output format")
def download_table(table: str, output: str) -> None:
    if output not in ["csv", "excel", "parquet"]:
        print("Unsupported output format, use csv, excel or parquet")
        return

    df = delta_sharing.load_as_pandas(f"config.share#{table}")
    if output == "csv":
        print("Writing to data.csv")
        df.to_csv("data.csv")
    elif output == "excel":
        print("Writing to data.xlsx")
        # Excel cannot handle timezone aware timestamps
        df.timestamp = df.timestamp.dt.tz_localize(None)
        df.event_timestamp = df.event_timestamp.dt.tz_localize(None)
        df.to_excel("data.xlsx")
    elif output == "parquet":
        print("Writing to data.parquet")
        df.to_parquet("data.parquet")


if __name__ == "__main__":
    cli()
    print("All done")

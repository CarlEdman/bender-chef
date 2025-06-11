#! python3
import plexapi
import click


@click.group()
@click.version_option()
@click.option("-c", "--clobber/--no-clobber", default=False)  # "if necessary, overwrite existing items."
@click.option("-m", "--move/--copy", default=False)  # "delete originals of transferred items."
@click.option("-d", "--dryrun/--live", default=False)  #  "do not perform operations, but only print them.


@click.option("--user-name", type=str)
@click.option("--password", type=str)
@click.option("--server-base-url", type=str)
@click.option("--server-token", type=str)
@click.option("--client-base-url", type=str)
@click.option("--client-token", type=str)
@click.option("--container-size", type=int)
@click.option("--timeout", type=float)

def main(clobber, move, dryrun, user_name, password, server_base_url, server_token, client_base_url, client_token, container_size, timeout):
    """CLI to Plex REST API"""
    click.echo("CLI")


@main.group()
def watchlist():
    """Manage users' centrally-stored watchlist."""
    click.echo("watchlist")


@watchlist.command("import")
@click.argument("id", type=int)
def watchlist_import(id):
    """Ingest a watchlist to User ID from stdin in JSON format."""
    click.echo("import")


@watchlist.command("export")
@click.argument("id", type=int)
def watchlist_export(id):
    """Dump a watchlist of User ID to stdout in JSON format."""
    click.echo("export")


@watchlist.command("transfer")
@click.argument("from_id", type=int)
@click.argument("to_id", type=int)
def watchlist_transfer(from_id, to_id):
    """Move all watchlist items of User FROM_ID to user TO_ID."""
    click.echo("transfer")


if __name__ == "__main__":
    pass


# log = logging.getLogger()

# parser = argparse.ArgumentParser(
#     fromfile_prefix_chars="@", prog=prog, epilog="Written by: " + author
# )

# parser.add_argument(
#     "--debug",
#     dest="loglevel",
#     action="store_const",
#     const=logging.DEBUG,
#     help="print debugging (or higher) log messages.",
# )

# parser.add_argument(
#     "--taciturn",
#     dest="loglevel",
#     action="store_const",
#     const=logging.ERROR,
#     help="only print error level (or higher) log messages.",
# )

# parser.add_argument(
#     "--log", dest="logfile", action="store", help="location of alternate log file."
# )

# parser.set_defaults(loglevel=logging.WARN)

# commands_parser = parser.add_subparsers(dest="command", help="Available commands")

# for i in [
#     (pathlib.Path.home() / ".config" / prog).with_suffix(".ini"),
#     pathlib.Path(sys.argv[0]).with_suffix(".ini"),
#     pathlib.Path(prog).with_suffix(".ini"),
#     (pathlib.Path("..") / prog).with_suffix(".ini"),
# ]:
#     if i.exists():
#         sys.argv.insert(1, f"@{i}")

# args = parser.parse_args()

# if args.dryrun and args.loglevel > logging.INFO:
#     args.loglevel = logging.INFO

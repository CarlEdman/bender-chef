#! python3
import logging

import click
import plexapi
from plexapi.myplex import MyPlexAccount, PlexServer


@click.group()
@click.version_option()
@click.option(
    "-c",
    "--clobber/--no-clobber",
    default=False,
    help="if necessary, overwrite existing items.",
)
@click.option(
    "--move/--copy",
    "move",
    default=False,
    help="move items.  (i.e., remove original items if successfully transferred elsewhere).",
)
@click.option(
    "--dryrun",
    "dryrun",
    default=False,
    help="do not perform operations, but only print them.",
)
@click.option(
    "--debug",
    "loglevel",
    flag_value=logging.DEBUG,
    help="print debugging (or higher level) log messages.",
)
@click.option(
    "--verbose",
    "loglevel",
    flag_value=logging.VERBOSE,
    help="print informational (or higher level) log messages.",
)
@click.option(
    "--taciturn",
    "loglevel",
    flag_value=logging.ERROR,
    help="print only error (or higher level) log messages.",
)
@click.option("--user-name", type=str)
@click.option("--password", type=str)
@click.option("--server-base-url", type=str)
@click.option("--server-token", type=str)
@click.option("--client-base-url", type=str)
@click.option("--client-token", type=str)
@click.option("--container-size", type=int)
@click.option("--timeout", type=float)
def main(
    clobber,
    move,
    dryrun,
    user_name,
    password,
    server_base_url,
    server_token,
    client_base_url,
    client_token,
    container_size,
    timeout,
    loglevel,
):
    """CLI to Plex REST API"""
    click.echo("CLI")


@main.group()
def watchlist():
    """Manage users' centrally-stored watchlist."""
    click.echo("watchlist")


@watchlist.command("import")
@click.argument("token", type=int)
def watchlist_import(token):
    """Ingest a watchlist to User TOKEN from stdin in JSON format."""
    click.echo("import")


@watchlist.command("export")
@click.argument("token", type=int)
def watchlist_export(token):
    """Dump a watchlist of User TOKEN to stdout in JSON format."""
    click.echo("export")
    account = MyPlexAccount()
    for i in account.watchlist(sort="name:asc"):
        click.echo(repr(i))


#    plex = account.resource('<SERVERNAME>').connect()  # returns a PlexServer instance
# plex = PlexServer()
# for video in plex.library.section("Movies").search(unwatched=True):
#    print(video.title)


@watchlist.command("transfer")
@click.argument("from_token", type=int)
@click.argument("to_token", type=int)
def watchlist_transfer(from_token, to_token):
    """Move all watchlist items of User FROM_TOKEN to user TO_TOKEN."""
    click.echo("transfer")


@main.group()
def history():
    """Manage users' local history."""
    click.echo("history")


@history.command("import")
@click.argument("token", type=int)
def history_import(token):
    """Ingest watch history to User TOKEN from stdin in JSON format."""
    click.echo("import")


@history.command("export")
@click.argument("token", type=int)
def history_export(token):
    """Dump a watch history of User TOKEN to stdout in JSON format."""
    click.echo("export")
    # account = MyPlexAccount()
    # for i in account.history(sort="name:asc"):
    #     click.echo(repr(i))


#    plex = account.resource('<SERVERNAME>').connect()  # returns a PlexServer instance
# plex = PlexServer()
# for video in plex.library.section("Movies").search(unwatched=True):
#    print(video.title)


@history.command("transfer")
@click.argument("from_token", type=int)
@click.argument("to_token", type=int)
def history_transfer(from_token, to_token):
    """Move all history from User FROM_TOKEN to User TO_TOKEN."""
    click.echo("transfer")


# log = logging.getLogger()

# parser = argparse.ArgumentParser(
#     fromfile_prefix_chars="@", prog=prog, epilog="Written by: " + author
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

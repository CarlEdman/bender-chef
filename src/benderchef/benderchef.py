#! python3
import logging
import click
import plexapi
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer

log = logging.getLogger()

plex = None


class BenderChefGlobal:
    user_name = None

    def get_user_name():
        return BenderChefGlobal.user_name

    def set_user_name(user_name):
        BenderChefGlobal.user_name = user_name

    password = None

    def get_password():
        return BenderChefGlobal.password

    def set_password(password):
        BenderChefGlobal.password = password

    server_name = None

    def get_server_name():
        return BenderChefGlobal.server_name

    def set_server_name(server_name):
        BenderChefGlobal.server_name = server_name

    account = None

    def get_account():
        if BenderChefGlobal.account is None:
            try:
                BenderChefGlobal.account = MyPlexAccount(
                    BenderChefGlobal.user_name, BenderChefGlobal.password
                )
            except Exception:
                pass

        return BenderChefGlobal.account

    def set_account(account):
        BenderChefGlobal.account = account

    plex = None

    def get_plex():
        if BenderChefGlobal.plex is None:
            try:
                BenderChefGlobal.plex = (
                    BenderChefGlobal.get_account()
                    .resource(BenderChefGlobal.get_server_name())
                    .connect()
                )

            except Exception:
                pass
        if BenderChefGlobal.plex is None:
            try:
                BenderChefGlobal.plex = PlexServer(
                    BenderChefGlobal.get_base_url(), BenderChefGlobal.get_token()
                )
            except Exception:
                pass
        return BenderChefGlobal.plex

    def set_plex(plex):
        BenderChefGlobal.plex = plex

        # if plex is None:
        #     logging.critical(
        #         "Could not establish connection to a server either through user_name, password, and server_name, or through server_base_url and server_token."
        #     )
        #     raise plexapi.exceptions.Unauthorized()


@click.group(
    context_settings={"auto_envvar_prefix": "BENDER_CHEF"},
    epilog="See https://github.com/CarlEdman/bender-chef for more details",
)
@click.version_option()
@click.option(
    "-c",
    "--clobber/--no-clobber",
    default=False,
    help="If necessary, overwrite existing items.",
)
@click.option(
    "-m",
    "--move/--copy",
    "move",
    default=False,
    help="Move items (i.e., remove original items if successfully transferred elsewhere).",
)
@click.option(
    "-d",
    "--dryrun/--liverun",
    "dryrun",
    default=False,
    help="Do not perform operations, but only print them.",
)
@click.option(
    "--debug",
    "loglevel",
    default=logging.WARNING,
    flag_value=logging.DEBUG,
    help="Print debugging (or higher level) log messages.",
)
@click.option(
    "--verbose",
    "loglevel",
    flag_value=logging.INFO,
    help="Print informational (or higher level) log messages.",
)
@click.option(
    "--taciturn",
    "loglevel",
    flag_value=logging.ERROR,
    help="Print only error (or higher level) log messages.",
)
@click.option(
    "--user-name", type=str, help="User name used to log in to https://plex.tv."
)
@click.option(
    "--password", type=str, help="Password used to log in to https://plex.tv."
)
@click.option(
    "--server-base-url",
    type=str,
    help="URL of local Plex server to be used, e.g., https://plex.example.com:32400.",
)
@click.option(
    "--server-token",
    type=str,
    help="""Token used by owner of server to identify and authenticate.
Instructions for retrieval are at https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/.""",
)
@click.option(
    "--server-name",
    type=str,
    help="""Owner-given name of local server to work on.""",
)
@click.option("--client-base-url", type=str, help="Local Plex player's URL.")
@click.option(
    "--client-token",
    type=str,
    help="Token used to identify and authenticate individual plex user.",
)
@click.option(
    "--container-size",
    type=int,
    default=50,
    help="Number of items to request with each plex server call.  Should only affect performance, not results.",
)
@click.option(
    "--timeout",
    type=float,
    help="Timeout for server requests in seconds.  No effect unless servers or connection are overloaded.",
)
def main(
    clobber,
    move,
    dryrun,
    user_name,
    password,
    server_base_url,
    server_token,
    server_name,
    client_base_url,
    client_token,
    container_size,
    timeout,
    loglevel,
):
    """CLI to Plex REST API.

    \b
    Options can be set via environment variables, e.g., like this:
        export BENDER_CHEF_USER_NAME=MeMeMeMe
        export BENDER_CHEF_CLOBBER=True

    Much more to come.
    """
    click.echo("CLI")

    if dryrun:
        loglevel = max(logging.INFO, loglevel)
    log.setLevel(loglevel)


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
    account = plexapi.myplex.MyPlexAccount()
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
    # account = plexapi.myplex.MyPlexAccount()
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


@main.group()
def token():
    """Manage users' tokens."""


@token.command("get")
def token_get():
    """Obtain token corresponding to currently specified (or default) user and password."""

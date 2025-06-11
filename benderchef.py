#! python3
import plexapi
import argparse
import logging
import logging.handlers
import pathlib
import os
import sys
# import clink

prog = "plexchef"
version = "0.01"
author = "Carl Edman (CarlEdman@gmail.com)"
desc = "CLI tool to provide missing Plex functionality through the REST API."

log = logging.getLogger()

parser = argparse.ArgumentParser(
    fromfile_prefix_chars="@", prog=prog, epilog="Written by: " + author
)

parser.add_argument(
    "-d",
    "--dryrun",
    dest="dryrun",
    action="store_true",
    help="do not perform operations, but only print them.",
)

parser.add_argument("--version", action="version", version="%(prog)s " + version)
parser.add_argument(
    "--verbose",
    dest="loglevel",
    action="store_const",
    const=logging.INFO,
    help="print informational (or higher) log messages.",
)

parser.add_argument(
    "--debug",
    dest="loglevel",
    action="store_const",
    const=logging.DEBUG,
    help="print debugging (or higher) log messages.",
)

parser.add_argument(
    "--taciturn",
    dest="loglevel",
    action="store_const",
    const=logging.ERROR,
    help="only print error level (or higher) log messages.",
)

parser.add_argument(
    "--log", dest="logfile", action="store", help="location of alternate log file."
)

parser.set_defaults(loglevel=logging.WARN)

commands_parser = parser.add_subparsers(dest="command", help="Available commands")

watchlist_parser = commands_parser.add_parser(
    "watchlist", help="Manage users' centrally-stored watchlist."
)

watchlist_command_parser = watchlist_parser.add_parser(
    "watchlist_command", help="Subcommands for watchlist command parser."
)

watchlist_import_parser = watchlist_command_parser.add_parser(
    "watchlist_import", help="Ingest a watchlist from stdin in JSON format."
)

watchlist_export_parser = watchlist_command_parser.add_parser(
    "watchlist_export", help="Dump a watchlist to stdout in JSON format."
)

watchlist_transfer_parser = watchlist_command_parser.add_parser(
    "watchlist_transfer", help="Move all watchlist items of user A to user B."
)

watchlist_transfer_parser.add_argument(
  "-f", "--force", "--clobber",
  dest="watchlist_transfer_clobber",
  action="store_true",
  help="overwrite existing watchlist items.",
)

for i in [
    (pathlib.Path.home() / ".config" / prog).with_suffix(".ini"),
    pathlib.Path(sys.argv[0]).with_suffix(".ini"),
    pathlib.Path(prog).with_suffix(".ini"),
    (pathlib.Path("..") / prog).with_suffix(".ini"),
]:
    if i.exists():
        sys.argv.insert(1, f"@{i}")

args = parser.parse_args()

if args.dryrun and args.loglevel > logging.INFO:
    args.loglevel = logging.INFO


if __name__ == "__main__":
  pass

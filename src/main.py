import os
import sys
import click

from pathlib import Path


VERSION = "0.1.0"
CONTEXT_SETTINGS = dict(auto_envvar_prefix="COVID")
HOME = str(Path.home())


# Callback function to print version message.
def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.secho("covid version: v%s" % VERSION, fg="blue")
    ctx.exit()


# Determine the color based on log level.
def log_level(argument):
    switcher = {
        "info": "green",
        "warn": "yellow",
        "error": "red",
        "debug": "normal",
        "fancy": "blue",
        "verbose": "reset",
    }
    return switcher.get(argument, "green")


class Environment(object):
    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
        self.obj = {}

    def log(self, msg, *args, **kwargs):
        """Logs a message to stderr."""
        if args:
            msg %= args

        level = kwargs.get("level", "info")
        color = log_level(level)

        click.secho(msg, file=sys.stderr, fg=color)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, level="verbose", *args)

    def set_value(self, key, value):
        """Set an arbitrary value to a specified key for future lookup."""
        self.obj[key] = value

    def get_value(self, key):
        """Get the value of a specified key lookup."""
        return self.obj[key]


pass_environment = click.make_pass_decorator(Environment, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))


class COVID_CLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode("ascii", "replace")
            mod = __import__("src.commands.cmd_" + name, None, None, ["cli"])
        except Exception as e:
            print(e)
        except ImportError:
            return

        if mod.cli is None:
            print(mod)

        return mod.cli


@click.command(cls=COVID_CLI, context_settings=CONTEXT_SETTINGS)
@click.option(
    "--home",
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    help="Project folder to operate on.",
)
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Print the current version of bessy.",
)
@pass_environment
def cli(ctx, verbose, home):
    """
    Covid is a tool to run data ingestion, serve it via a REST
    API, and visualize the data.
    """
    ctx.verbose = verbose
    if home is not None:
        ctx.home = home

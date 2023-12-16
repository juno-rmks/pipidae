""" Pipidae の CLI (Command Line Interface) です。
"""
import click

from . import __version__


@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, default=False, help="バージョンを表示して終了します。")
@click.pass_context
def cli(ctx: click.Context, version: bool):
    """Pipidae は Python モジュールです。\f

    `--version` オプションを指定した場合、バージョンを表示してコマンドの実行を終了します。

    サブコマンドの指定がない場合、ヘルプを表示してコマンドの実行を終了します。

    Parameters
    ----------
    ctx: click.Context
        click コマンドのコンテキストです。
    version: bool
        バージョンを表示して終了するかどうかです。
    """
    if version:
        click.echo(f"Pipidae {__version__}")
        ctx.exit()

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()

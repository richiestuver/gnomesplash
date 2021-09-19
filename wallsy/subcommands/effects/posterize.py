from pathlib import Path

import click

from wallsy import image_handler
from wallsy.cli_utils.decorators import *
from wallsy.cli_utils.console import *


@click.command(name="posterize")
@click.option(
    "--colors",
    default=32,
    show_default=True,
    help="Specify the number of colors to reduce the image to (range 1-255)",
)
@make_callback
@make_generator
@catch_errors
@require_file
def cli(file: Path, colors: int):
    """
    Apply a posterization effect to the image.
    """

    describe(f":sparkler-emoji: 'poster' applying poster effect to '{file.name}'...")
    file = image_handler.quantize(file, path_modifier="posterize", colors=colors)
    confirm_success(
        f":floppy_disk-emoji: 'poster' saved image as '{file.name}' in {file.parent}"
    )
    return file

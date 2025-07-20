#!/usr/bin/env python3

import sys
import click
from PIL import Image

ASCII_CHARS = ['@', '#', '%', '?', '*', '+', ';', ':', ',', '.', ' ']

def convert_image(image_path, new_width=75):
    image = Image.open(image_path).convert('L')  # 转灰度
    image = image.resize((new_width, int(new_width * image.height / image.width / 2))) # mono font, a char w:h = 1:2
    pixels = image.getdata()
    ascii_str = ''.join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return '\n'.join([ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)])


@click.command()
@click.option('-w', '--width', type=int, default=75, show_default=True, help='specify the width of the ASCII art')
@click.help_option('-h', '--help')
@click.version_option(None, '-v', '--version')
@click.argument('file', nargs=1, type=click.Path(exists=True))
def main(width:int, file: str) -> None:
    click.echo(convert_image(file, width))

if __name__ == "__main__":
    main()

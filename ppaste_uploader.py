"""

Usage:
    ppaste_uploader.py <filename> [-l <lang>] [-s <start>] [-e <end>]

Options:
    -h --help                           Show this screen
    -l <language>, --lang=<language>    Language of the file
    -s <start>, --start=<start>         Start line
    -e <end>, --end=<end>               End line

"""
from docopt import docopt

import utils


def main(args, lexers):
    print(args)
    try:
        with open(args['<filename>'], "r") as f:
            lines = f.readlines()
    except IOError:
        print("Error when opening the file")
        print(__doc__)
    else:
        title = "Test"
        language = utils.get_language(lexers, args)
        lines = utils.slice_lines(lines, args)
        is_private = False
        paste_url = utils.send_paste(
            "".join(lines),
            title,
            language,
            is_private
        )
        print(paste_url)


if __name__ == "__main__":
    args = docopt(__doc__, version='ppaste_uploader 0.3')
    lexers = utils.read_lexers()
    main(args, lexers)

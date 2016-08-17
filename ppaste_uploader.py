import sys

import utils


def main(argv, lexers):
    filename = argv[0]
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except IOError:
        print("Error when opening the file")
        utils.usage()
    else:
        title = "Test"
        language = utils.get_lexer(filename, lexers)
        print(language)
        is_private = False
        paste_url = utils.send_paste(
            "".join(lines),
            title,
            language,
            is_private
        )
        print(paste_url)


if __name__ == "__main__":
    lexers = utils.read_lexers()
    # Better command line arguments handling to be made with
    main(sys.argv[1:], lexers)

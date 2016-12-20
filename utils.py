import json

import requests


def send_paste(content, title, language, is_private):
    data = {
        'pastecontent': content,
        'title': title,
        'hl': language,
    }
    if is_private:
        data['privatepaste'] = "true"
    # URL not hardcoded in the ~near feature
    response = requests.post('http://127.0.0.1:8088/submit', data=data)
    return response.url


def read_lexers():
    """
    Read all the lexers from the LEXERS file, and store them in a dict.
    Sometimes, the same extension can be used for different file formats.
    To prevent loss of information, we store everything in a list.
    We then have to ask or warn that the file type cannot be determined
    by the file extension.
    """
    try:
        with open("LEXERS", "r") as f:
            d = json.loads(''.join(f.readlines()))
    except IOError:
        print("Could not open LEXER file")
    return d


def get_language(lexers, args):
    """
    Computes the language requested. If a language is passed in the arguments,
    we pick this one. Otherwise, we try to compute it from the extension name.
    If no filename is found, or the filename doesn't match anything, returns
    the string text.
    """
    if args.get('--lang') is not None:
        return args['--lang']
    filename = args['<filename>']
    t = filename.split('.')
    if len(t) == 1:  # No extension name
        return 'text'
    lexer = lexers.get(t[-1])  # Defaults to text
    if lexer is None:
        return 'text'
    return lexer


def slice_lines(lines, args):
    s = args.get('--start')
    e = args.get('--end')
    if s is None:
        s = 1
    else:
        s = int(s)
    if e is None:
        e = len(lines)
    else:
        e = int(e)
    return lines[s - 1:e]

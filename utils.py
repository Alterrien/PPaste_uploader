import json

import requests


def usage():
    print("ppaste_uploader")
    print("Usage : ppaste_uploader.py <filename>")


def send_paste(content, title, language, is_private):
    if is_private:
        private = "true"
    else:
        private = "false"
    data = {
        'pastecontent': content,
        'title': title,
        'hl': language,
        'privatepaste': private
    }
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
    lexers = {}
    try:
        with open("LEXERS", "r") as f:
            return json.loads(''.join(f.readlines()))
    except IOError:
        print("Could not open LEXER file")


def get_lexer(filename, lexers):
    """
    Returns (for now) the first lexer associated with the extension of the
    filename passed as a parameter
    If no filename is found, or the filename doesn't match anything, returns
    the string text
    """
    t = filename.split('.')
    if len(t) == 1:  # No extension name
        return 'text'
    lexer = lexers.get(t[-1])  # Defaults to text
    if lexer is None:
        return 'text'
    return lexer

import sys

import requests


def usage():
    print("ppaste_uploader")
    print("Usage : ppaste_uploader.py <filename>")


def send_paste(lines, title, language, is_private):
    if is_private:
        private = "true"
    else:
        private = "false"
    data = {
        'content': "".join(lines).replace(" ", "+"),
        'title': title,
        'hl': "text",
        'privatepaste': private
    }
    response = requests.post('http://127.0.0.1:8088/submit', data=data)
    return response.url


def main(argv):
    file_name = argv[0]
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
        title = ""
        language = "Text only"
        is_private = False
        paste_url = send_paste(
            lines,
            title,
            language,
            is_private
        )
        print(paste_url)
    except IOError:
        print("Error when opening the file")
        usage()


if __name__ == "__main__":
    main(sys.argv[1:])

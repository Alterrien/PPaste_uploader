import json

from pygments.lexers import get_all_lexers

if __name__ == "__main__":
    lexers = get_all_lexers()
    d = {}
    for lexer in lexers:
        hl = lexer[1][0]
        exts = lexer[2]
        for ext in exts:
            stripped_ext = ext.split(".")[-1]
            if stripped_ext in d:
                d[stripped_ext].append(hl)
            else:
                d[stripped_ext] = [hl]
    with open("../LEXERS", "w") as f:
        f.write(json.dumps(d))

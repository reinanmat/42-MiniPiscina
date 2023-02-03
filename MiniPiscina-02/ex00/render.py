import sys
import re

def check_args(argv):
    if (len(argv) == 1 or len(argv) > 2):
        sys.exit(1)
    if (re.search(".template", argv[1]) == None):
        sys.exit(1)

def open_template(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return (lines)

def open_settings():
    with open("settings.py", "r") as file:
        splited = file.read().split("\n")
        dct = {}
        for i in splited:
            dct[i.split(" = ")[0].strip(' ')] = i.split(" = ")[1].strip(' "')
    return (dct)

def main():
    check_args(sys.argv)
    template = open_template(sys.argv[1])
    settings = open_settings()
    format_template = template.format(**settings)
    print(format_template)
    with open("index.html", "w") as file:
        file.write(format_template)

if __name__ == '__main__':
    main()


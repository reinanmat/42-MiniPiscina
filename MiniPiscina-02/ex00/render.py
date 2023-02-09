import sys
import os
import re

def check_args(argv):
    if (len(argv) == 1 or len(argv) > 2):
        sys.exit("Error: wrong number of arguments")
    if (re.search(".template", argv[1]) == None):
        sys.exit("Error: wrong file extension")
    if not (os.path.isfile(argv[1])):
        sys.exit("Error: file does not exist")

def open_template(filename):
    with open(filename, "r") as file:
        lines = file.read()
    return (lines)

def open_settings():
    with open("settings.py", "r") as file:
        splited = list(filter(None, file.read().split("\n")))
        dct = {}
        for i in splited:
            dct[i.split(" = ")[0].strip(' ')] = i.split(" = ")[1].strip(' "')
    return (dct)

def main():
    check_args(sys.argv)
    template = open_template(sys.argv[1])
    settings = open_settings()
    try:
        format_template = template.format(**settings)
    except:
        sys.exit("Error: unexpected error in .template or settings.py")
    with open(sys.argv[1].replace(".template", ".html"), "w") as file:
        file.write(format_template)

if __name__ == '__main__':
    main()


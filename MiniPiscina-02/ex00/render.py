import sys

def check_args(argv):
    if (len(argv) > 2):
        sys.exit(1)
    if (argv[1].find('.template') == -1):
        sys.exit(1)

def html(msg):
    with open("cv.html", "w") as file:
        file.write('<!DOCTYPE>\n')
        file.write('<html lang="en">\n')
        file.write('<head>\n')
        file.write('    <meta charset="utf-8>\n')
        file.write('    <title>Title</title>\n')
        file.write('</head>\n')
        file.write('<body>\n')
        file.write(f'   {msg}\n')
        file.write('</body>\n')
        file.write('</html>')

def open_file(filename):
    with open(filename, "r") as file:
        msg = file.read()
        html(msg)

def main():
    check_args(sys.argv)
    open_file(sys.argv[1])

if __name__ == '__main__':
    main()


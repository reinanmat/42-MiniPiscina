def numbers():
    with open("numbers.txt", "r") as fd:
        txt = fd.read().split(",")
    for line in txt:
        print(line)

if  __name__ == '__main__':
    numbers()

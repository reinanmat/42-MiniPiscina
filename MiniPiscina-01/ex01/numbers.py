def numbers():
    file = open("numbers.txt")
    txt = file.read()
    tab = txt.split(",")
    for i in tab:
        print(i)
    file.close()

if  __name__ == '__main__':
    numbers()

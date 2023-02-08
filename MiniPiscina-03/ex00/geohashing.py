import sys

def main():
    hash1 = hash(sys.argv[1])
    hash2 = hash(sys.argv[2])
    hash3 = hash(sys.argv[3])
    print(hash1)
    print(hash2)
    print(hash3)

if __name__ == '__main__':
    main()

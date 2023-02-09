import sys
import antigravity

def check_args():
    if (len(sys.argv) != 4):
        sys.exit("Error: wrong number of arguments")

def main():
    check_args()
    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])
    date = sys.argv[3].encode('utf-8')
    antigravity.geohash(latitude, longitude, date)

if __name__ == '__main__':
    main()

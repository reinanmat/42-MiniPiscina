import sys
import antigravity

def check_args():
    if (len(sys.argv) != 4):
        sys.exit("Error: wrong number of arguments")

def main():
    check_args()
    try:
        latitude = float(sys.argv[1])
    except:
        sys.exit("Error: Invalid latitude")
    try:
        longitude = float(sys.argv[2])
    except:
        sys.exit("Error: Invalid latitude")
    try:
        date = sys.argv[3].encode('utf-8')
    except:
        sys.exit("Error: Invalid date")
    antigravity.geohash(latitude, longitude, date)

if __name__ == '__main__':
    main()

import sys

def check_args():
    if len(sys.argv) != 2:
        sys.exit()

def state_main():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    for i in capital_cities:
        if (sys.argv[1] == capital_cities[i]):
            for j in states:
                if i == states[j]:
                    print(j)
                    sys.exit()
    print("Unknown capital city")

if __name__ == '__main__':
    check_args()
    state_main()

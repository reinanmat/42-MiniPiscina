import  sys

def check_args():
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        sys.exit()

def capital_main():
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
    if (sys.argv[1] in states):
        print(capital_cities[states[sys.argv[1]]])
    else:
        print("Unknow state")

if  __name__ == '__main__':
    check_args()
    capital_main()

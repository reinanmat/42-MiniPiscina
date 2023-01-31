import sys

def check_args():
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        sys.exit()

def seach_value(capital, capital_cities):
    for i in capital_cities:
        if capital == capital_cities[i]:
            return i
    return 0

def find_city(sig, states):
    for i in states:
        if states[i] == sig:
            print(i)

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
    sig = seach_value(sys.argv[1], capital_cities)
    if sig == 0:
        return (print("Unkown capital city"))
    find_city(sig, states)
    
if __name__ == '__main__':
    check_args()
    state_main()

import  sys

def check_args():
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        sys.exit()

def find_state(state, states):
    for i in states:
        if i == state:
            return states[i]
    return 0

def find_capital(city, capital_cities):
    for i in capital_cities:
        if i == city:
            print(capital_cities[i])

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

    city = find_state(sys.argv[1], states)
    if city == 0:
        return(print("Unknow state"))
    find_capital(city, capital_cities)

if  __name__ == '__main__':
    check_args()
    capital_main()

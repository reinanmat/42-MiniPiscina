import sys

def check_args():
    if len(sys.argv) == 1 or len(sys.argv) > 2:
        sys.exit()

def state_or_capital(index, states, capital_cities):
    if str in states:
        return state
    for i in capital_cities:
        if capital_cities[i] == index:
            return capital
    return 0

def discover_state(capital, states, capital_cities):
    for i in capital_cities:
        if capital == capital_cities[i]:
            sig = i
    for i in states:
        if sig == i:
            state = i
    print(f"{capital} is the capital of {state}")

def discover_capital(state, states, capital_cities):
    for i in states:
        if i == state:
            sig = state[i]

    for i in capital_cities:
        if sig == i:
            state = capital_cities[i]

def all_in():
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
    lst = sys.argv[1].split(", ")
    for i in lst:
        ret = state_or_capital(lst[i], states, capital_cities)
        if ret == state:    
           discover_state(i, states, capital_cities) 
        if ret == capital:
           discover_capital(i, states, capital_cities) 
        else:
            print(f"{i} is neither a capital city nor a state")
    print(lst)

if __name__ == '__main__':
    check_args()
    all_in()


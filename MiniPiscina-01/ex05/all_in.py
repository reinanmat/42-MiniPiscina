import sys

def check_args(arg):
    if (len(arg) == 1 or len(arg) > 2):
        sys.exit()

def find_state(capital, states, capital_cities):
    for i in capital_cities:
        if (capital == capital_cities[i]):
            for j in states:
                if i == states[j]:
                    return (j)

def find_capital_city(state, states, capital_cities):
    return (capital_cities[states[state]])

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
    splited = sys.argv[1].split(',')
    striped = [x.strip() for x in splited]
    lst = filter(None, striped)
    for i in lst:
        if i.title() in states:
            print(f"{find_capital_city(i.title(), states, capital_cities)} is the capital city of {i.title()}")
        elif (find_state(i.title(), states, capital_cities)):
            print(f"{i.title()} is the capital city of {find_state(i.title(), states, capital_cities)}")
        else:
            print(f"{i} is neither a capital city nor a state")

if __name__ == '__main__':
    check_args(sys.argv)
    all_in()


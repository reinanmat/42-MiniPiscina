import random
from beverages import *

class CoffeeMachine:
    def __init__(self):
        self.drinks_served = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            super().__init__(name = "empty cup", price = 0.90)

        def description(self):
            return("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self):
            raise Exception("This This coffee machine has to be repaired.")

    def repair(self):
        self.drinks_served = 0

    def server(self, drink):
        self.drinks_served += 1
        if (self.drinks_served > 10): 
            self.BrokenMachineException()
        empty = self.EmptyCup()
        self.beverages = [empty, drink]
        return (random.choice(self.beverages))

def main():
    coffee_machine = CoffeeMachine()
    beverages = [Coffee(), Tea(), Chocolate(), Cappucciono()]
    for i in range(11):
        try:
            print(f"beverage : {i + 1}°")
            print(coffee_machine.server(random.choice(beverages)))
            print("\n")
        except Exception as msg:
            print("============================================")
            print(f"{msg}")
            print("============================================\n")
    coffee_machine.repair()
    for i in range(11):
        try:
            print(f"beverage : {i + 1}°")
            print(coffee_machine.server(random.choice(beverages)))
            print("\n")
        except Exception as msg:
            print("============================================")
            print(f"{msg}")
            print("============================================\n")

if __name__ == '__main__':
    main()

         
    

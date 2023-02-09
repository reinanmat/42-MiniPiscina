class HotBeverage:
    def __init__(self, name = "hot beverage", price = 0.30):
        self.price = price
        self.name = name

    def description(self):
        return ("Just some hot water in a cup.")

    def __str__(self):
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(name = "coffee", price = 0.40)

    def description(self):
        return ("A coffee, to stay awake.")

class Tea(HotBeverage):
    def __init__(self):
        super().__init__(name = "tea")

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(name = "chocolate", price = 0.50)

    def description(self):
        return ("Chocolate, sweet chocolate...")

class Cappucciono(HotBeverage):
    def __init__(self):
        super().__init__(name = "cappuccino", price = 0.45)

    def description(self):
        return ("Un po’ di Italia nella sua tazza!")

def main():
    beverage1 = HotBeverage()
    print(f"{beverage1}\n")
    beverage2 = Coffee()
    print(f"{beverage2}\n")
    beverage3 = Tea()
    print(f"{beverage3}\n")
    beverage4 = Chocolate()
    print(f"{beverage4}\n")
    beverage5 = Cappucciono()
    print(f"{beverage5}\n")

if __name__ == '__main__':
    main()



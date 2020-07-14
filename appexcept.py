# try:
#     pass
# except expression as identifier:
#     pass
# else:
#     pass
# finally:
#     pass
class Investment:
    def __init__(self, id, name, balance):
        self.__id = id
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @classmethod
    def get_instance(self):
        return self(0, 0, 200)

    def __eq__(self, other):
        return self.__balance == other.__balance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value != "":
            self.__name = value


class Stock(Investment):
    def __init__(self, id, balance):
        super().__init__(id, "Stock", balance)


inv = Investment(1, "Bond", 300)
inv_stucks = Investment(2, "Stucks", 300)
inv_defualt = Investment.get_instance()
inv.name = ""


print(inv.name)
print(inv.balance)
print(inv_defualt.balance)
print(inv == inv_defualt)
print(inv_stucks == inv)


stockInv = Stock(10, 100)

print(stockInv.balance)

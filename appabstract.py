from abc import ABC, abstractmethod


class Investment(ABC):
    @abstractmethod
    def get_All_Funds(self):
        pass


class Bond(Investment):
    def get_balance(self):
        return 1000

    def get_All_Funds(self):
        return "Bond"


st = Bond()
print(st.get_balance())

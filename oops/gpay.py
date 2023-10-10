from abc import ABC,abstractmethod

class bankingapp(ABC):
    
    @abstractmethod
    def fundtransfer(self):
        pass

    @abstractmethod
    def balanceenquiry(self):
        pass

    @abstractmethod
    def transactionhistory(self):
        pass


class gpay(bankingapp):

    def fundtransfer(self):
        print("gpay fundtransfer")

    def balanceenquiry(self):
        print("gpay balanceenquiry")

    def transactionhistory(self):
        print("gpay transactionhistory")

obj=gpay()
obj.fundtransfer()
obj.balanceenquiry()
obj.transactionhistory()
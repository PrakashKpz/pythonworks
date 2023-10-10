from datetime import datetime
class bank:
    bank_name:set
    acno:str
    person_name:str
    ac_type:str
    balance:int
    
    def create(self,b_name,acno,p_name,ac_type,bal):
        self.bank_name=b_name
        self.acno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal

    def deposit(self,amount):
        self.balance+=amount
        print(f"your {self.bank_name} has been credited with {amount} avl bal is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("transaction failed")
        else:
            self.balance-=amount
            print(f"your {self.bank_name} has been debited with {amount} avl bal is {self.balance}")
   
    def get_balance(self):
        print(f"your {self.bank_name} a\c {self.acno} bal on {datetime.today()} avl bal is {self.balance} ")

obj1=bank()
obj1.create("sbi","002","kishor","selfie",50)

obj1.deposit(2000)
obj1.withdraw(3000)
obj1.get_balance()

obj2=bank()
obj2.create("sbi","002","reng","selfie",60)


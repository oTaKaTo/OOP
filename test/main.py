from enum import Enum
from abc import ABC,abstractclassmethod,abstractstaticmethod,abstractmethod


class User:
    def __init__(self,name:str , PIN:str , account_no:str):
        self.__name = name
        self.__PIN = PIN
        self.__account_no = account_no

    def get_PIN(self):
        return self.__PIN
    
    def get_account_no(self):
        return self.__account_no

class ATMCard:
    def __init__(self,card_number:str,name:str,account_no:str,exp:str):
        self.__card_no = card_number
        self.__name = name
        self.__account_no = account_no
        self.__expired_date = exp

    def get_account_no(self):
        return self.__account_no

class Account:
    def __init__(self, account_no:str,balance:int):
        self.__balance = balance
        self.__account_no = ""
        self.__history = []

    def get_balance(self):
        return self.__balance
    
    def update_balance(self,type:str ,amount:int):
        if type == "Withdraw" or type == "Transfer":
            self.__balance -= amount
        elif type == "Deposit" or type == "Receive":
            self.__balance += amount
        self.__history.append(History(type,amount,"11.40 AM 25/04/2566","success"))
        return True 
    
    def get_account_no(self):
        return self.__account_no

class History:
    def __init__(self,type:str ,amount:int ,date:str,status:str):
        self.__type = type
        self.__amount = amount
        self.__date = date
        self.__status = status



class Bank:
    def __init__(self,name:str,no:str):
        self.__name = ""
        self.__no = ""
        self.__accounts = []
        self.__users = []


    def get_accounts(self):
        return self.__accounts
    
    def get_account_by_no(self,no:str):
        for i in self.__accounts:
            if no in i.get_account_no():
                return i
        print("Account Incorrect")
        return True
    
    def get_user_by_no(self,no:str):
        for i in self.__users:
            if no in i.get_account_no():
                return i
        print("User Incorrect")
        return True
    
    def add_account(self,account:Account):
        for i in self.__accounts:
            if account.get_account_no() in i.get_account_no():
                print("This account has already existed !!!")
                return True
        self.__accounts.append(account)
        print(f"Add {account.get_account_no()} success !!!")    
        return True
    
    def add_user(self,user:User):
        for i in self.__users:
            if user.get_account_no() in i.get_account_no():
                print("This user has already existed !!!")
                return True
        self.__users.append(user)
        print(f"Add {user.get_account_no()} success !!!")    
        return True
    
    def check_PIN(self,account_no:str,PIN:str):
        user = self.get_user_by_no(account_no)
        if user.get_PIN() == PIN:
            return True
        print("Invalid PIN")


class ATM:
    def __init__(self,ATM_no:str,quan_100:int = 100 ,quan_500:int =100 ,quan_1000:int= 100):
        self.__ATM_no = ATM_no
        self.__cash_100 = quan_100
        self.__cash_500 = quan_500
        self.__cash_1000 = quan_1000
        self.__total_cash = 0
    
    def calc_total (self):
        self.__total_cash = (self.__cash_100 * 100)+(self.__cash_500*500)+(self.__cash_1000*1000)

    def get_total_cash(self):
        self.calc_total()
        return self.__total_cash
    
    def withdraw_cash(self,amount:int):
            cash_1000_amount = amount//1000
            amount = amount - (cash_1000_amount*1000)
            print(amount)
            cash_500_amount = amount//500
            amount = amount - (cash_500_amount*500)
            print(amount)
            cash_100_amount = amount // 100

            if cash_1000_amount > self.__cash_1000 or cash_500_amount > self.__cash_500 or cash_100_amount > self.__cash_100:
                print("Not enough cash !!!")
                return True
            elif cash_1000_amount <= self.__cash_1000 or cash_500_amount <= self.__cash_500 or cash_100_amount <= self.__cash_100:
                print("Here you are")
                print(f"Number of 1000 bills : {cash_1000_amount}")
                print(f"Number of 500 bills : {cash_500_amount}")
                print(f"Number of 100 bills : {cash_100_amount}")
                self.__cash_1000 -= cash_1000_amount 
                self.__cash_500 -= cash_500_amount
                self.__cash_100 -= cash_100_amount
                return True
            
    def deposite_cash(self,amount_1000:int, amount_500:int ,amount_100:int):
        self.__cash_1000 += amount_1000
        self.__cash_500 += amount_500
        self.__cash_100 += amount_100
        print("Your deposite has been received")
    
    def read_card(self,user:User,card:ATMCard,bank:Bank):
        acc_no = card.get_account_no()
        print('aDSDAS')
        input_pin = input("Enter Your PIN : ")
        return bank.check_PIN(acc_no,input_pin)
        
        


#Transaction
class Transaction:
    @abstractmethod
    def process(self,account:Account,atm:ATM):
        pass

class WithdrawCash(Transaction):
    def __init__(self):
        pass
    def process(self,account:Account,atm:ATM):
        print(f"Available Balance : {account.get_balance()}")
        withdraw_amount = int(input("Enter amount to withdraw : "))
        print(atm.get_total_cash())
        if atm.get_total_cash() < withdraw_amount:
            print("Not enough cash !!!")
        elif account.get_balance() < withdraw_amount:
            print("Not enough money in your account!!!")
        elif  account.get_balance() >= withdraw_amount:
            if atm.withdraw_cash(withdraw_amount):
                account.update_balance("Withdraw",withdraw_amount)
        print(f"Balance : {account.get_balance()}")


class DepositeCash(Transaction):
    def __init__(self):
        pass
    def process(self,account:Account,atm:ATM):
        print(f"Available Balance : {account.get_balance()}")
        deposit_amount = int(input("Enter amount to Deposite : "))
        bill_1000  = int(input("Number of 1000 bills : "))
        bill_500 = int(input("Number of 500 bills : "))
        bill_100 = int(input("Number of 100 bills : "))
        atm.deposite_cash(bill_1000,bill_500,bill_100)
        account.update_balance("Deposit",deposit_amount)
        print(f"Balance : {account.get_balance()}")
        

class TransferMoney(Transaction):
    def __init__(self):
        pass

    def check_transfer_number(self,tranfer_no: str,bank:Bank):
        for i in bank.get_accounts():
            if tranfer_no in i.get_account_no(): 
                return i
        return False  
    
    def tranfer_money(self,account:Account,account_to_transfer:Account,transfer_amount:int):
        account.update_balance("Transfer",transfer_amount)
        account_to_transfer.update_balance("Receive",transfer_amount)
        print(f"Transfer to Account number {account_to_transfer.get_account_no} success !!!")

    def process(self,account:Account,bank:Bank):
        print(f"Available Balance : {account.get_balance()}")
        transfer_number = input("Enter transfer account number : ")
        if self.check_transfer_number(transfer_number,bank):
            account_2_tranfer = self.check_transfer_number(transfer_number,bank)
            transfer_amount = int(input("Enter amount to Transfer : "))
            self.tranfer_money(account,account_2_tranfer,transfer_amount)
        else:
            print("Invalid Tranfer Account !!!")
            
        print(f"Balance : {account.get_balance()}")



KBonkaw = Bank("KBonkaw","65010373")
KBonk = ATM("65010373",100,100,100)
my_acc = Account("65010373",1000)
acc2 = Account("65010374",1000)
my_acc_card = ATMCard("65010373","Takdanai Deephuak","65010373","1/01/2032")
my_user = User("Takdanai Deephuak","0373","65010373")
User2 = User("Matte Glutter","0374","65010374")
withdraw = WithdrawCash()
deposit = DepositeCash()
transfer = TransferMoney()
KBonkaw.add_account(my_acc)
KBonkaw.add_account(acc2)
KBonkaw.add_user(my_user)
KBonkaw.add_user(User2)
while True:
    insert_card = input("Please insert your card (Y/N):")
    if insert_card.lower() == 'y':
        if KBonk.read_card(my_user,my_acc_card,KBonkaw):
            print("Select transaction :")
            print("1. Withdraw Cash")
            print("2. Deposite Cash")
            print("3. Transfer Money")
            select = input("transaction (1,2,3) : ")
            if select == "1":
                withdraw.process(my_acc,KBonk)
            elif select == "2":
                deposit.process(my_acc,KBonk)
            elif select == "3":
                transfer.process(my_acc,KBonk)


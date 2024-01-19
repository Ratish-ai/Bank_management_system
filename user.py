import db

class greetings:
    def __init__(self,name) -> None:
        print(f"Welcome {name} !!!!")

class admin:
    pass

class user:
    def __init__(self,u_id) -> None:
        self.u_id = u_id
        self.sql = db.user()
        self.home()
    
    def home(self):
        print("1. Deposit\n2. Withdraw\n3. Transfer amount\n4. View Statement\n5. Logout")
        try:
            self.option = int(input("Enter your Choice : "))
        except:
            print("Enter a numerical value !!!!")
            self.home()
        else:
            if self.option==1:
                self.deposit()
            elif self.option==2:
                self.withdraw()
            elif self.option==3:
                self.transfer()
            elif self.option==4:
                self.view_transfer()
            elif self.option==5:
                return
            else:
                print("Enter a Correct option !!!!")
                self.home()
    
    def deposit(self):
        amt = int(input("Enter the amount to deposit : "))
    
    def withdraw(self):
        amt = int(input("Enter the amount to withdraw : "))
    
    def transfer(self):
        acc = input("Enter the account number to transfer the money : ")
        amt = int(input("Enter the amount to transfer : "))
    
    def view_transfer(self):
        pass
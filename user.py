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
        self.sql.deposit(self.u_id,amt)
    
    def withdraw(self):
        amt = int(input("Enter the amount to withdraw : "))
        if self.sql.withdraw(self.u_id,amt):
            def amount():
                print("1. Re-enter the amount\n2. Go Back")
                try:
                    option = int(input("Enter your option : "))
                except:
                    print("Enter numerical value !!!!")
                else:
                    if option==1:
                        amount()
                    elif option==2:
                        return self.home()
                    else:
                        print("Enter a valid number !!!!!!")
                        amount()
            amount()

    def transfer(self):
        acc = input("Enter the account number to transfer the money : ")
        if self.sql.acc(acc):
            print("Account not found")
            def account():
                print("1. Re-enter the account number\n2. Go Back")
                option = input("Enter your option : ")
                if option==1:
                    account()
                elif option==2:
                    return self.home()
                else:
                    print("Enter a valid number !!!!!!")
                    account()
            account()
        amt = int(input("Enter the amount to transfer : "))
        if self.sql.withdraw(self.u_id,amt):
            def amount():
                print("1. Re-enter the amount\n2. Go Back")
                try:
                    option = int(input("Enter your option : "))
                except:
                    print("Enter numerical value !!!!")
                else:
                    if option==1:
                        amount()
                    elif option==2:
                        return self.home()
                    else:
                        print("Enter a valid number !!!!!!")
                        amount()
            amount()
        self.sql.transfer(self.u_id,acc,amt)
    
    def view_transfer(self):
        pass
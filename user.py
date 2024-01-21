import db

class greetings:
    def __init__(self,name) -> None:
        print(f"Welcome {name} !!!!")

class admin:
    def __init__(self):
        self.sql = db.admin()
        self.home()
    
    def home(self):
        print("1. Add Account\n2. Remove Account\n3. View all account details\n4. View a particular account detail\n\n5. Logout\n")
        try:
            option = input("Enter your option : ")
        except:
            print("Enter a numerical value !!!!!")
            self.home()
        else:
            if option==1:
                self.add_acc()
            elif option==2:
                self.remove_acc()
            elif option==3:
                self.view_all()
                self.home()
            elif option==4:
                self.view_particular()
                self.home()
            elif option==5:
                return
            else:
                print("Enter a correct option !!!!!")
                self.home()
    
    def add_acc(self):
        pass

    def remove_acc(self):
        acc_no = input("Enter the account number to be deleted !!!!")
        def step():
            print(f'\nVerify the account number : {acc_no}\n\n1. Correct\n2. Wrong')
            try:
                option = int(input('Enter your option : '))
            except:
                print("Enter a numerical value !!!!")
                step()
            else:
                if option==1:
                    self.sql.remove_acc(acc_no)
                elif option==2:
                    print("1. Re-enter account number\n2. Go Back\n")
                    option = int(input('Enter your option : '))
                    if option==1:
                        self.remove_acc()
                    elif option==2:
                        self.home()
                    else:
                        step()
        step()
        self.sql.remove(acc_no)
        print("Account removed Succesfully !!!")
    
    def view_all(self):
        self.sql.view_all()
    
    def view_particular(self):
        acc_no = input("Enter the account number to be deleted !!!!")
        def step():
            print(f'\nVerify the account number : {acc_no}\n\n1. Correct\n2. Wrong')
            try:
                option = int(input('Enter your option : '))
            except:
                print("Enter a numerical value !!!!")
                step()
            else:
                if option==1:
                    self.sql.remove_acc(acc_no)
                elif option==2:
                    print("1. Re-enter account number\n2. Go Back\n")
                    option = int(input('Enter your option : '))
                    if option==1:
                        self.remove_acc()
                    elif option==2:
                        self.home()
                    else:
                        step()
        step()
        self.sql.view_acc(acc_no)

class user:
    def __init__(self,u_id) -> None:
        self.u_id = u_id
        self.sql = db.user()
        self.home()
    
    def home(self):
        print("1. Deposit\n2. Withdraw\n3. Transfer amount\n4. View Statement\n5. View Balance\n6. Logout")
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
                self.balance()
                self.home()
            elif self.option==6:
                return
            else:
                print("Enter a Correct option !!!!")
                self.home()
    
    def deposit(self):
        amt = int(input("Enter the amount to deposit : "))
        t_id = self.sql.generate_transaction_id()
        self.sql.deposit(self.u_id,amt)
        to_acc = self.sql.acc_no(self.u_id)
        self.sql.transaction(t_id,'self',to_acc,amt)
        self.sql.credit_transfer(t_id,to_acc)
    
    def withdraw(self):
        amt = int(input("Enter the amount to withdraw : "))
        bal = self.sql.balance(self.u_id)
        if bal<amt:
            print("Insufficient Balance")
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
        t_id = self.sql.generate_transaction_id()
        self.sql.withdraw(self.u_id,amt)
        from_acc = self.sql.acc_no(self.u_id)
        self.sql.transaction(t_id,from_acc,'self',amt)
        self.sql.debit_transfer(t_id,from_acc)

    def transfer(self):
        acc = input("Enter the account number to transfer the money : ")
        if self.sql.acc(acc):
            print("Account not found !!!!!!")
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
        bal = self.sql.balance(self.u_id)
        if bal<amt:
            print("Insufficient Balance")
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
        self.balance()
        self.sql.view_transactions(self.u_id)
    
    def balance(self):
        bal = self.sql.balance(self.u_id)
        print(f"Current balance : {bal}")
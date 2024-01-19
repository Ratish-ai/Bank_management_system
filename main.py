import db
import user
import operations

sql = db.login()

class first():
    def __init__(self) -> None:
        print("--------------- WELCOME TO THE BANK ---------------")
        print("1. Sign Up\n2. Sign In\n3. Exit\n")
        try:
            self.option = int(input("Enter your Choice : "))
        except:
            print("Enter a numerical value !!!!")
            first()
        else:
            if self.option==1:
                self.signup()
            elif self.option==2:
                self.signin()
            elif self.option==3:
                print("--------------- THANK YOU ---------------")
                exit()
            else:
                print("Enter a Correct option !!!!")
                first()
    
    def signup(self):
        user_name = input("Enter your user name given by the bank admin : ")
        if sql.user_name_validate(user_name):
            def password():
                print("Password Constraints :\n1. Should have at least one number.\n2. Should have at least one uppercase and one lowercase character.\n3. Should have at least one special symbol.\n4. Should be between 6 to 16 characters long.")
                self.pwd = input("Enter your password : ")
                if operations.password_validate(self.pwd):
                    print("Password is invalid !!!!!! ")
                    def next():
                        print("1. Re-enter password\n2. Go back\n3. Exit")
                        try:
                            ans = int(input("Enter your choice : "))
                        except:
                            print("Enter a numerical value !!!!")
                            next()
                        else:
                            if ans==1:
                                password()
                            elif ans==2:
                                return first()
                            elif ans==3:
                                exit()
                            else:
                                print("Enter a valid number !!!!")
                                next()
                    next()
            password()
            def conf_password():
                pwd = input("Confirm your password : ")
                if pwd!=self.pwd:
                    print("Enter correct password !!!!!")
                    conf_password()
            conf_password()
            sql.user_pass(user_name,self.pwd)
            print("Password set successfully !!!")
        else:
            print("Invalid user !!!!")
            def next():
                print("1. Re-enter user name\n2. Go back\n3. Exit")
                try:
                    ans = int(input("Enter your choice : "))
                except:
                    print("Enter a numerical value !!!!")
                    next()
                else:
                    if ans==1:
                        self.signup()
                    elif ans==2:
                        return
                    elif ans==3:
                        exit()
                    else:
                        print("Enter a valid number !!!!")
                        next()
            next()

    def signin(self):
        user_name = input("Enter your user name : ")
        if sql.user_name_check(user_name):
            def password():
                pwd = input("Enter your password : ")
                if not sql.password_check(user_name,pwd):
                    print("Password is invalid !!!!!! ")
                    def next():
                        print("1. Re-enter password\n2. Go back\n3. Exit")
                        try:
                            ans = int(input("Enter your choice : "))
                        except:
                            print("Enter a numerical value !!!!")
                            next()
                        else:
                            if ans==1:
                                password()
                            elif ans==2:
                                return first()
                            elif ans==3:
                                exit()
                            else:
                                print("Enter a valid number !!!!")
                                next()
                    next()
            password()
            user.greetings(sql.name(user_name))
            user_type = sql.user_type(user_name)
            if user_type=='admin':
                user.admin()
            else:
                user.user(sql.user_id(user_name))
        else:
            print("Invalid user !!!!")
            def next():
                print("1. Re-enter user name\n2. Go back\n3. Exit")
                try:
                    ans = int(input("Enter your choice : "))
                except:
                    print("Enter a numerical value !!!!")
                    next()
                else:
                    if ans==1:
                        self.signup()
                    elif ans==2:
                        return 
                    elif ans==3:
                        exit()
                    else:
                        print("Enter a valid number !!!!")
                        next()
            next()

if __name__ == '__main__':
    while True:
        first()
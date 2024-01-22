import db
import user
import operations

sql = db.login()

class first():
    def __init__(self) -> None:
        print("\n\n\n--------------- WELCOME TO THE BANK ---------------\n\n\n")
        print("1. Sign Up\n2. Sign In\n3. Exit\n\n")
        try:
            self.option = int(input("Enter your Choice : "))
        except:
            print("\n\nEnter a numerical value !!!!\n\n")
            first()
        else:
            if self.option==1:
                self.signup()
            elif self.option==2:
                self.signin()
            elif self.option==3:
                print("\n\n\n--------------- THANK YOU ---------------\n\n\n")
                exit()
            else:
                print("\n\nEnter a Correct option !!!!\n\n")
                first()
    
    def signup(self):
        user_name = input("\nEnter your user name given by the bank admin : ")
        if sql.user_name_validate(user_name):
            def password():
                print("\nPassword Constraints :\n1. Should have at least one number.\n2. Should have at least one uppercase and one lowercase character.\n3. Should have at least one special symbol.\n4. Should be between 6 to 16 characters long.\n")
                self.pwd = input("\nEnter your password : ")
                if operations.password_validate(self.pwd):
                    print("\n\nPassword is invalid !!!!!! \n\n")
                    def next():
                        print("\n1. Re-enter password\n2. Go back\n3. Exit\n")
                        try:
                            ans = int(input("\nEnter your choice : "))
                        except:
                            print("\n\nEnter a numerical value !!!!\n\n")
                            next()
                        else:
                            if ans==1:
                                password()
                            elif ans==2:
                                return first()
                            elif ans==3:
                                exit()
                            else:
                                print("\n\nEnter a valid number !!!!\n\n")
                                next()
                    next()
            password()
            def conf_password():
                pwd = input("\n\nConfirm your password : ")
                if pwd!=self.pwd:
                    print("\n\nEnter correct password !!!!!\n\n")
                    conf_password()
            conf_password()
            sql.user_pass(user_name,self.pwd)
            print("\nPassword set successfully !!!\n\n")
        else:
            print("\n\nInvalid user !!!!\n\n")
            def next():
                print("1. Re-enter user name\n2. Go back\n3. Exit\n")
                try:
                    ans = int(input("Enter your choice : "))
                except:
                    print("\n\nEnter a numerical value !!!!\n\n")
                    next()
                else:
                    if ans==1:
                        self.signup()
                    elif ans==2:
                        return
                    elif ans==3:
                        exit()
                    else:
                        print("\n\nEnter a valid number !!!!\n\n")
                        next()
            next()

    def signin(self):
        user_name = input("\n\nEnter your user name : ")
        if sql.user_name_check(user_name):
            def password():
                pwd = input("\n\nEnter your password : ")
                if not sql.password_check(user_name,pwd):
                    print("\n\nPassword is invalid !!!!!! \n\n")
                    def next():
                        print("\n\n1. Re-enter password\n2. Go back\n3. Exit\n\n")
                        try:
                            ans = int(input("Enter your choice : "))
                        except:
                            print("\n\nEnter a numerical value !!!!\n\n")
                            next()
                        else:
                            if ans==1:
                                password()
                            elif ans==2:
                                return first()
                            elif ans==3:
                                exit()
                            else:
                                print("\n\nEnter a valid number !!!!\n\n")
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
            print("\n\nInvalid user !!!!\n\n")
            def next():
                print("\n\n1. Re-enter user name\n2. Go back\n3. Exit\n\n")
                try:
                    ans = int(input("Enter your choice : "))
                except:
                    print("\n\nEnter a numerical value !!!!\n\n")
                    next()
                else:
                    if ans==1:
                        self.signin()
                    elif ans==2:
                        return 
                    elif ans==3:
                        exit()
                    else:
                        print("\n\nEnter a valid number !!!!\n\n")
                        next()
            next()

if __name__ == '__main__':
    while True:
        first()
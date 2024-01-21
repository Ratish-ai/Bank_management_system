import mysql.connector
import operations

class sql:
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ratish^2",
            database="bank"
        )

        self.mycursor = self.mydb.cursor()

class login(sql):
    
    def __init__(self):
        super().__init__()
    
    def user_name_validate(self,u_name):
        query = f"SELECT * FROM user_details WHERE user_name = '{u_name}'"
        self.mycursor.execute(query)
        self.result = self.mycursor.fetchall()
        print(self.result)
        return self.result!=None
    
    def user_pass(self,u_name,pwd):
        query = f"SELECT * FROM user_details WHERE user_name = '{u_name}'"
        self.mycursor.execute(query)
        self.result = self.mycursor.fetchone()
        u_id = self.result[0]
        name = self.result[1]
        query = f"INSERT INTO user_login (user_id,name,user_name,password,user_type) VALUES ({u_id},'{name}','{u_name}','{pwd}','user')"
        self.mycursor.execute(query)
        self.mydb.commit()
    
    def user_name_check(self,u_name):
        query = f"SELECT * FROM user_login WHERE user_name = '{u_name}';"
        self.mycursor.execute(query)
        self.result = self.mycursor.fetchone()
        return u_name in self.result
    
    def password_check(self,u_name,pwd):
        query = f"SELECT password FROM user_login WHERE user_name = '{u_name}';"
        self.mycursor.execute(query)
        self.result = self.mycursor.fetchone()
        return pwd in self.result
    
    def user_type(self,u_name):
        query = f"SELECT user_type FROM user_login WHERE user_name = '{u_name}';"
        self.mycursor.execute(query)
        self.result = self.mycursor.fetchone()
        return self.result[0]
    
    def name(self,u_name):
        query = f"SELECT name FROM user_login WHERE user_name = '{u_name}';"
        self.mycursor.execute(query)
        self.result = self.mycursor.fetchone()
        return self.result[0]
    
    def user_id(self,u_name):
        query = f"SELECT user_id FROM user_login WHERE user_name = '{u_name}';"
        self.mycursor.execute(query)
        self.result = self.mycursor.fetchone()
        return self.result[0]

class user(sql):
    def __init__(self):
        super().__init__()
    
    def balance(self,u_id):
        query = f"SELECT balance FROM user_details WHERE user_id = {u_id};"
        self.mycursor.execute(query)
        bal = self.mycursor.fetchone()[0]
        return bal
    
    def deposit(self,u_id,amt,t_id=None):
        bal = self.balance(u_id)
        nb = bal+amt
        query = f"UPDATE user_details SET balance = {nb} WHERE user_id = {u_id};"
        self.mycursor.execute(query)
        self.mydb.commit()
        if t_id is None:
            t_id = self.generate_transaction_id()
        acc = self.acc_no(u_id)
        self.credit_transfer(t_id,acc)
        return t_id
    
    def withdraw(self,u_id,amt,t_id=None):
        bal = self.balance(u_id)
        nb = bal-amt
        query = f"UPDATE user_details SET balance = {nb} WHERE user_id = {u_id};"
        self.mycursor.execute(query)
        self.mydb.commit()
        if t_id is None:
            t_id = self.generate_transaction_id()
        acc = self.acc_no(u_id)
        self.debit_transfer(t_id,acc)
        return t_id
    
    def acc(self,acc):
        query = f"SELECT acc_no FROM user_details WHERE acc_no = '{acc}';"
        self.mycursor.execute(query)
        bal = self.mycursor.fetchone()
        return bal==None
    
    def generate_transaction_id(self):
        query = f"SELECT MAX(transaction_id) FROM transaction;"
        self.mycursor.execute(query)
        res = self.mycursor.fetchone()
        if res is None or res[0] is None:
            return 1
        return res[0]+1
    
    def acc_no(self,u_id):
        query = f"select acc_no from user_details where user_id = {u_id}"
        self.mycursor.execute(query)
        return self.mycursor.fetchone()[0]
    
    def debit_transfer(self,t_id,from_acc):
        query = f"INSERT INTO transaction_details (transaction_id,acc,type) VALUES ({t_id},'{from_acc}','debit')"
        self.mycursor.execute(query)
        self.mydb.commit()
    
    def credit_transfer(self,t_id,to_acc):
        query = f"INSERT INTO transaction_details (transaction_id,acc,type) VALUES ({t_id},'{to_acc}','credit')"
        self.mycursor.execute(query)
        self.mydb.commit()
    
    def find_uid(self,acc):
        query = f"SELECT user_id FROM user_details WHERE acc_no='{acc}'"
        self.mycursor.execute(query)
        return self.mycursor.fetchone()[0]
    
    def transfer(self,from_u_id,to_acc,amt):
        from_acc = self.acc_no(from_u_id)
        to_u_id = self.find_uid(to_acc)
        t_id = self.generate_transaction_id()
        self.deposit(to_u_id,amt,t_id)
        self.withdraw(from_u_id,amt,t_id)
        self.transaction(t_id,from_acc,to_acc,amt)
    
    def transaction(self,t_id,from_acc,to_acc,amt):
        date = operations.today_date()
        time = operations.now_time()
        query = f"INSERT INTO transaction (transaction_id,by,to,date,time,amt) VALUES ({t_id},'{from_acc}','{to_acc}','{date}','{time}',{amt})"
        self.mycursor.execute(query)
        self.mydb.commit()
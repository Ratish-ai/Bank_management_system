import re
from datetime import datetime
import random

def password_validate(pwd):
    reg = "^.*(?=.{6,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    pat = re.compile(reg)             
    mat = re.search(pat, pwd)
    return not mat

def today_date():
    date = datetime.now()
    return str(date).split()[0]
    
def now_time():
    time = str(datetime.now()).split()[1]
    time = time.split(':')
    time[2] = str(int(eval(time[2])))
    return ':'.join(time)

def generate_acc_no():
    n = random.randint(1000000000000000,9999999999999999)
    return str(n)

def generate_user_name(name,ph):
    name = name.strip().split()[0]
    return name+ph[:5]
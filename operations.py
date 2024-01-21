import re
from datetime import datetime

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
    time[2] = str(int(time[2]))
    return ':'.join(time)
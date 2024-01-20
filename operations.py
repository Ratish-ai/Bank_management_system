import re

def password_validate(pwd):
    reg = "^.*(?=.{6,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    pat = re.compile(reg)             
    mat = re.search(pat, pwd)
    return not mat

def change_time(time):
    time = time.split(':')[:2]
    return ':'.join(time)
import re

def password_validate(self,pwd):
    reg = "^.*(?=.{6,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    pat = re.compile(reg)             
    mat = re.search(pat, pwd)
    return not mat
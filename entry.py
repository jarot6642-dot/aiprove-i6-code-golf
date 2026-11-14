import re
def e(s):return eval(s,{})if re.fullmatch('[0-9+*/(). -]+',s)and'**'not in s and'//'not in s else (_ for _ in ()).throw(ValueError('bad'))

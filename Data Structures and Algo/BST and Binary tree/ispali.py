def isPali(str):
    if len(str) < 2: 
        return True
    if(str[0] == str[-1]):
        return isPali(str[1:-1])
    else:
        return False

myS = "aba"
print(isPali(myS))
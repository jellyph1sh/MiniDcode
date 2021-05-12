#coding:utf-8

# -- technique --

def usable(code):
    code = ' '.join((' '.join(str(code).split('\n'))).split('\r')).split(' ')
    return [und_code for und_code in code if und_code != ' ' and und_code != '']

def checkbase(code, base):
    for und_code in code:
        for part in und_code:
            if not part in base:
                return False
    return True

# -- base 2  --

def isbin(code):
    return checkbase(code, '01\n\r ')

def binindec(code):
    retour = []
    for und_code in usable(code):
        i, result = 0, 0
        for bit in str(und_code)[::-1]:
            result += int(bit)*2**i
            i += 1
        retour.append(str(result))
    return retour

def decinbin(code):
    retour = []
    for und_code in code:
        und_code, result = int(und_code), ''
        while und_code != 0:
            result += str(und_code%2)
            und_code = und_code//2
        retour.append(result[::-1])
    return ' '.join(retour)

# -- base 8  --

def isoct(code):
    return checkbase(code, '01234567\n\r ')

def octindec(code):
    retour = []
    for und_code in usable(code):
        i, result = 0, 0
        for bit in str(und_code)[::-1]:
            result += int(bit)*8**i
            i += 1
        retour.append(str(result))
    return retour

def decinoct(code):
    retour = []
    for und_code in code:
        und_code, result = int(und_code), ''
        while und_code != 0:
            result += str(und_code%8)
            und_code = und_code//8
        retour.append(result[::-1])
    return ' '.join(retour)

# -- base 10 --

def isdec(code):
    return checkbase(code, '0123456879\n\r ')

def decindec(code):
    return ' '.join(code)

# -- base 16 --

def ishex(code):
    return checkbase(code, '0123456789abcdef\n\r ')

def hexindec(code):
    retour = []
    for und_code in usable(code):
        letters = {
            '0':0,'1':1,'2':2,'3':3,
            '4':4,'5':5,'6':6,'7':7,
            '8':8,'9':9,'a':10,'b':11,
            'c':12,'d':13,'e':14,'f':15
        }
        i, result = 0, 0
        for part in und_code[::-1]:
            result += letters[part]*16**i
            i += 1
        retour.append(str(result))
    return retour

def decinhex(code):
    retour = []
    for und_code in code:
        letters = {
           0:'0',1:'1',2:'2',3:'3',
           4:'4',5:'5',6:'6',7:'7',
           8:'8',9:'9',10:'a',11:'b',
           12:'c',13:'d',14:'e',15:'f'
        }
        und_code, result = int(und_code), ''
        while und_code != 0:
            result += str(letters[und_code%16])
            und_code = und_code//16
        retour.append(result[::-1])
    return ' '.join(retour)

# -- ASCII --

def isasc(code):
    for und_code in code:
        try:
            if not 0 <= int(und_code) <= 127:
                return False
        except:
            for part in str(und_code):
                if not 0 <= int(ord(part)) <= 127:
                    return False
    return True

def ascindec(code):
    retour = []
    for char in code:
        retour.append(str(ord(char)))
    return retour

def decinasc(code):
    retour = []
    for char in code:
        retour.append(chr(int(char)))
    return ''.join(retour)

# -- GENERAL --

def otherindec(code, base):
    if base == 'bsbin':
        if isbin(code):
            return 'FROM 2 TO 10', binindec(code)
        return ['ERREUR', 'Un des nombres n\'est pas en base 2'], ''
    elif base == 'bsoct':
        if isoct(code):
            return 'FROM 8 TO 10', octindec(code)
        return ['ERREUR', 'Un des nombres n\'est pas en base 8'], ''
    elif base == 'bsdec':
        if isdec(code):
            return 'FROM 10 TO 10', usable(code)
        return ['ERREUR', 'Un des nombres n\'est pas en base 10'], ''
    elif base == 'bshex':
        if ishex(code.lower()):
            return 'FROM 16 TO 10', hexindec(code.lower())
        return ['ERREUR', 'Un des nombres n\'est pas en base 16'], ''
    elif base == 'bsasc':
        if isasc(code):
            return 'FROM ASCII TO 10', ascindec(code)
        return ['ERREUR', 'Un des caractères n\'appartient à la table ASCII'], ''
    return ['ERREUR', 'Base non prise en compte'], ''

def decinother(code, base):
    if isdec(code):
        if base == 'bsbin':
            return 'FROM 10 TO 2', decinbin(code)
        elif base == 'bsoct':
            return 'FROM 10 TO 8', decinoct(code)
        elif base == 'bsdec':
            return 'FROM 10 TO 10', decindec(code)
        elif base == 'bshex':
            return 'FROM 10 TO 16', decinhex(code)
        elif base == 'bsasc':
            if isasc(code):
                return 'FROM 10 TO ASCII', decinasc(code)
            return ['ERREUR', 'Un des nombres n\'appartient à la table ASCII'], ''
        return ['ERREUR', 'Base non prise en compte'], ''
    return ['ERREUR', 'Un des nombres n\'est pas en base 10'], ''

def generalDcoding(code, baseA, baseB):
    readable = {
        'bsbin':'base 2', 'bsoct':'base 8',
        'bsdec':'base 10', 'bshex':'base 16',
        'bsasc':'ASCII'
    }
    alert, result = otherindec(code, baseA)
    if 'ERREUR' in alert:
        return alert[1], result
    alert, result = decinother(result, baseB)
    if 'ERREUR' in alert:
        return alert[1], result
    return f'De {readable[baseA]} en {readable[baseB]}', result
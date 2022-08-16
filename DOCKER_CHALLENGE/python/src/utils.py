from datetime import datetime
import hashlib

def formatDate(strDate):
    #Se usa el formato de fecha de la respuesta del json
    strDateTime = datetime.strptime(strDate,'%Y-%m-%dT%H:%M:%S.%fZ')
    return str(strDateTime)

def hashingPAN(strPAN):
    m = hashlib.sha256(strPAN.encode('utf-8')).hexdigest()
    stringhash = str(m)
    valcard = validcard(strPAN)
    if(valcard == "Invalid..."):
        return strPAN
    else:
        return stringhash



'''def truncatePAN(strPAN):
    #Se almacenan sólo los datos que cumplan con el formato XXXX-XXXX-XXXX-XXXX
    #Se valida el tamaño
    if(len(strPAN)==19):
        #Se valida que tenga 3 guiones (-)
        if(strPAN.count("-")==3):
            strPAN = "XXXX-XXXX-XXXX-"+strPAN[-4:]
            return strPAN
        else:
            return ""
    else:
        return ""'''

'''def validcard(N):
    N=N.replace('-', '')
    T=""; par=0;impar=0;X=""
    if not N.isdigit():return "1"
    if len(N) <14 or len(N)> 19: return "2"
    for c in range(0,len(N),2):       
        X=str(int(N[c])*2)       
        if len(X)==2:   
            par+=( int(X[0]) + int(X[1]) )
        else:par+=int(X)
    for c in range(1,len(N),2):
        impar+=int(N[c])
    if (par+impar)%10!=0:return "3"
    if int(N[0:2])>49 and int(N[0:2])<56:T="**MasterCard**"
    if N[0:2]=="34" or N[0:2]==37:T="**America Express**"
    if N[0]=="4":T="**VISA**"
    if N[0:2] in ["60","62","64","65"]:T="**Discover**"   
    return T'''

def isvalid(n):
    t=0
    for x,y in enumerate(reversed(n)):
        y=int(y)
        if x%2==1:
            y=y*2
            if y>=10:
                t+=y//10+y%10
            else:
                t+=y
        else:
            t+=y
    return t%10==0

def cardtype(n):
    a=int(n[0]);b=int(n[0:2])
    if b>49 and b<56:return '**MASTERCARD'
    if b==34 or b==37:return '**AMERICA EXPRESS'
    if b in [60,62,64,65]: return '**DISCOVER'
    if a==4: return '**VISA'
    return 'NONE--'

def validcard(N):
    N=N.replace('-', '')
    invalid = 'Invalid...'
    if isvalid(N)==True:
        return cardtype(N)
    else:
        return invalid



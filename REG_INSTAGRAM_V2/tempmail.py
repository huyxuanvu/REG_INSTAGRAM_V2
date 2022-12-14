import requests
import re
import time

rep = requests.session()

def getmail():
    request = rep.get("https://10minutemail.net/address.api.php?new=1")
    result = request.json()['mail_get_mail']
    return result

def getcode():
    count = 0 
    while True :          
        request000 = rep.get("https://10minutemail.net/address.api.php")       
        mail_list = request000.json()["mail_list"]
        for mail in mail_list :         
            if mail["from"] == '"Instagram" <no-reply@mail.instagram.com>' :
                sub = mail['subject']           
        if count == 30:
            break
        time.sleep(0.8)
        count += 1          
    regex  = re.findall(r'\d{1}',sub)
    code = ""
    for i in regex:
        code += str(i)
    return code


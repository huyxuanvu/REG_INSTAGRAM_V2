import random as rd
import json



with open("./data/firstName.txt" , 'r') as f:
     ho = f.read().strip().split('\n')
with open("./data/lastName.txt" , 'r') as f:
     ten = f.read().strip().split('\n')
with open("./data/settup.json",'r') as f :
     set = json.load(f)




def matkhau():
     str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890?/:|+_)(*&^$#@#!"
     pas = "".join(rd.sample(str,15))
     return pas

def name():
    t = rd.choice(ho) + ' ' +rd.choice(ten)
    return t

def username():
     
     str = "1234567890"
     user = rd.choice(ten) + set['UserName'] + "".join(rd.sample(str,3))
     return user

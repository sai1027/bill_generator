# connect with local database
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='pydb')
cursor=mydb.cursor()

from credentials import *
from store import *
from bill import *
from stock import *
import time
from os import system,name

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

# main
print('TEJA SUPERMARKET')
n=int(input('''
    1.login
    2.register(join membership for amazing discounts..)
    3.No thanks\n'''
    ))

if n==1:
    user_name=login(cursor)

elif n==2:
    status=register(cursor, mydb)
    if status:
        time.sleep(3)
        clear()
        user_name=login(cursor)

elif n==3:
    pass

elif n==123:
    status = staff(cursor)
    if status:
        time.sleep(3)
        clear()
        displayAll(cursor)
        addStock(cursor, mydb)
        exit()

time.sleep(3)
clear()
display(user_name , cursor)
shopping_bag=shop()
verifyBag = verifyBag(cursor,mydb, shopping_bag)
bill(verifyBag)

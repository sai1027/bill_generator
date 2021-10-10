import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='pydb')
cursor=mydb.cursor()

def login():
    user_name=input('user name : ')
    password=input('password : ')
    x='select cname from tejacus where cpassword=%s and cname=%s;'
    cursor.execute(x,(password,user_name,))
    s=cursor.fetchone()
    if s[0]==user_name:
        print("Login successfull..")
    else :
        print("login failed...")
        login()

def register():
    user_name=input('user name : ')
    x="select cname from tejacus where cname=%s;"
    cursor.execute(x,(user_name,))
    s=cursor.fetchall()
    if s:
        print("User name already exit. Try new..")
        register()
    password=input('password : ')
    mobile=int(input('mobile : '))

    x='insert into tejacus (cname,cpassword,cmobile) values(%s,%s,%s);'
    cursor.execute(x,(user_name,password,mobile,))
    mydb.commit()
    print("\nsuccessfull registered. pls login..\n")
    login()


def staff():
    user_name=input('user name : ')
    password=input('password : ')
    x='select ename from tejastaff where epassword=%s;'
    cursor.execute(x,(password,))
    s=cursor.fetchall()
    if s:
        print("Login successfull..")
    else :
        print("login failed...\ncontact manager \nyou dont have access..")
        exit()

def display():
    print("\nAvailable items at store : \n")
    print("-"*40)
    print('{:<10}{:<10}{:<10}{:<10}'.format('ITEM NO','ITEM','COST','QNT REMAING'))
    print("-"*40,'\n')

    cursor.execute('select itemno,item, cost, count from tejastock where count>0;')
    x=cursor.fetchall()
    for i in x:
        print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))
    print('\n',"-"*40,'\n')



def shop():
    print("enter 0 (zero) when done...")
    bag=[]
    while True:
        item=int(input('enter item number : '))
        if item==0:
            return bag
        qnt=int(input('enter quantity : '))

        bag.append([item,qnt])


def bill(b):

    for i in b:
        x='select item,cost,count from tejastock where itemno=%s;'
        cursor.execute(x,(i[0],))
        g=cursor.fetchone()

        s=int(g[2])
        p=int(i[1])
        qnt=min(s,p)
        item=g[0]
        cost=int(g[1])
        newBag=[]
        newBag.append([item,cost,qnt])

        if s > p :
            x=' update tejastock set count=%s where itemno=%s;'
            cursor.execute(x,(s-p,i[0],))
            mydb.commit()
        else :
            print(f"We have only {qnt} {g[0]}")
            x='update tejastock set count=%s where itemno=%s;'
            cursor.execute(x,(0,i[0],))
            mydb.commit()


    print('-'*50)
    print(' '*10,"TEJA SUPER MARKET")
    print('-'*50)
    print('\n')
    print('{:<10} {:<10} {:<10} {:<10} {:<10}'.format("S.NO" ,"ITEM" ,"MRP", "QUANTITY" ,"PRICE"))
    sno=0
    bill=0
    for i in newBag:
        sno+=1
        print('{:<10} {:<10} {:<10} {:<10} {:<10}'.format( sno,i[0] ,i[1], i[2] ,i[1]*i[2]))
        bill+=i[1]*i[2]

    print()
    print('-'*50)
    print(' '*30,"total bill = ",bill,' '*4)
    print('-'*50)
    print('thank u visit again  :)')
    print('\n\n')




# main
n=int(input("1.login\n2.register(join as new member for amazing discounts..)\n3.No thanks\n"))

if n==1:
    login()
elif n==2:
    register()
elif n==3:
    pass
elif n==123:
    staff()
    display()

display()
get_bill=shop()
bill(get_bill)

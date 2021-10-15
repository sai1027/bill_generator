# verifies account

def login(cursor):
    user_name=input('User name : ')

    password=input('Password : ')
    sql='select cname from customer where cpassword=%s and cname=%s;'
    cursor.execute(sql,(password,user_name,))
    data=cursor.fetchone()
    if data:
        print("Login successfull..")
        return user_name
    else :
        print("login failed...\ncheck user name and password again..")
        login(cursor)

def register(cursor, mydb):
    user_name=input('user name : ')
    sql="select cname from customer where cname=%s;"
    cursor.execute(sql,(user_name,))
    data=cursor.fetchall()
    if data:
        print("User name already exit. Try new..")
        register(cursor, mydb)
    else:
        password=input('Password : ')
        mobile=int(input('Mobile : '))
        email=input("Email : ")

        sql='insert into customer (cname,cpassword,cmobile,cemail) values(%s,%s,%s,%s);'
        cursor.execute(sql,(user_name,password,mobile,email,))
        mydb.commit()
        print("\nSuccessfull registered. Pls login..\n")
        
    return True


def staff(cursor):
    user_name=input('user name : ')
    password=input('password : ')
    sql='select ename from staff where epassword=%s and ename=%s;'
    cursor.execute(sql,(password,user_name,))
    data=cursor.fetchall()
    if data:
        print("Login successfull..")
        return True
    else :
        print("login failed...\ncontact manager \nyou dont have access..")
        exit()

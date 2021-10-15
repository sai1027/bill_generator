def displayAll(cursor):
    cursor.execute("select * from stock;")
    data=cursor.fetchall()

    print("{:<10}{:<10}{:<10}{:<10}".format('ITEMNO','ITEM','COST','QNT'))
    for i in data:
        print("{:<10}{:<10}{:<10}{:<10}".format(i[0],i[1],i[2],i[3]))




def addStock(cursor, mydb):

    flag = True
    print('\nMODE : \n1. Add qnt\n2. Add new item\n3. When done\n')

    while flag:
        n=int(input("Mode : "))
        if n==1:
            itemno=int(input("Enter itemno : "))
            quantity=int(input("Enter quantity : "))

            sql="update stock set qnt=qnt+%s where itemno=%s;"
            cursor.execute(sql,(quantity,itemno,))
            mydb.commit()

        elif n==2:
            item=input("Enter item name : ")
            cost = int(input("Enter cost : "))
            quantity=int(input("Enter quantity : "))

            sql="insert into stock(item,cost,qnt) values(%s,%s,%s);"
            cursor.execute(sql,(item,cost,quantity,))
            mydb.commit()

        elif n==3:
            flag= False


    print("\nStock after  update : \n")
    displayAll(cursor)

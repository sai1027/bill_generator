#  display the available stock
#  user can add items to bag and verifies items
from res import greet

def display(cursor, user_name):
    print(f'\n{greet()}{user_name}..\nWelcome to TEJA SUPERMARKET..\n')
    print("\nAvailable items at store : \n")
    print("-"*50)
    print('{:<10}{:<10}{:<10}{:<10}'.format('ITEM NO','ITEM','COST','QNT REMAING'))
    print("-"*50,'\n')

    cursor.execute('select itemno,item,cost,qnt from stock where qnt>0;')
    data=cursor.fetchall()
    for i in data:
        print('{:<10}{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2],i[3]))
    print('\n',"-"*50,'\n')



def shop():
    print("Enter 0 (zero) when done...")
    bag=[]
    while True:
        item=int(input('Enter item number : '))
        if item==0:
            return bag
        qnt=int(input('Enter quantity : '))

        bag.append([item,qnt])


def verifyBag(cursor, mydb, shopping_bag):
    newBag=[]
    for i in shopping_bag:
        sql='select item,cost,qnt from stock where itemno=%s;'
        cursor.execute(sql,(i[0],))
        data=cursor.fetchone()

        actualQnt=int(data[2])
        askedQnt=int(i[1])
        item=data[0]
        cost=int(data[1])
# TODO: error if item selcted is not displayed item.
        if actualQnt >= askedQnt :
            qnt=askedQnt

        else :
            qnt=actualQnt
            print(f"We have only {qnt} {data[0]}")


        sql='update stock set qnt=%s where itemno=%s;'
        cursor.execute(sql,(actualQnt-qnt,i[0],))
        mydb.commit()
        newBag.append([item,cost,qnt])

    return newBag

# here bill is generated.
from res import *
def bill(newBag, member):

    line()
    print(' '*15,"TEJA SUPER MARKET\n")
    print(f'Date : {day()}       Time : {time()}')
    line()
    print('{:<10} {:<10} {:<10} {:<10} {:<10}\n'.format("S.NO" ,"ITEM" ,"MRP", "QUANTITY" ,"PRICE"))

    sno=0
    billAmount=0

    for i in newBag:
        sno+=1
        print('{:<10} {:<10} {:<10} {:<10} {:<10}'.format( sno,i[0] ,i[1], i[2] ,i[1]*i[2]))
        billAmount+=i[1]*i[2]

    print("-"*55)
    print('{:>45}'.format(f'Bill = {billAmount}'))

    if member :
        Discount=discount(billAmount)
        print('{:>45}'.format(f'Discount = - {Discount}'))
        billAmount-=Discount

    Tax=tax(billAmount)
    print('{:>35}'.format(f'Tax (CGST + SGST) = + {Tax}'))
    billAmount+=Tax
    print('{:>35}'.format(f'Total Bill = {billAmount}'))
    line()
    print('Thank u visit again  :)')

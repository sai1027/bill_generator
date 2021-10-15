# here bill is generated.

def bill(newBag):

    print('-'*50)
    print(' '*10,"TEJA SUPER MARKET")
    print('-'*50)
    print('\n')
    print('{:<10} {:<10} {:<10} {:<10} {:<10}'.format("S.NO" ,"ITEM" ,"MRP", "QUANTITY" ,"PRICE"))

    sno=0
    billAmount=0

    for i in newBag:
        sno+=1
        print('{:<10} {:<10} {:<10} {:<10} {:<10}'.format( sno,i[0] ,i[1], i[2] ,i[1]*i[2]))
        billAmount+=i[1]*i[2]

    print()
    print('-'*50)
    print(' '*30,"total bill = ",billAmount,' '*4)
    print('-'*50)
    print('thank u visit again  :)')
    print('\n\n')

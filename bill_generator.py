# nv sai teja      reg.no:20113069

list={'pen':5,'pencil':5,'paper':10,'sketch':30,'file':50}
print("menu list : ",list)

cart=[]
item_quantity=[]
bill=0
ch='y'
item=1
while ch=='y' or ch=='Y':
    product=input("enter the product name : ")
    quantity=int(input("enter the quantity : "))
    bill+=(list[product])*quantity
    cart.append(product)
    item_quantity.append(quantity)

    ch=input("u want to add more y or n : ")
    item+=1




print()
print('-'*30)
print(' '*8,"bill",' '*8)
print('-'*30)
print()
print('S.NO  ITEM   MRP  QUANTITY   PRICE')
for i in range(0,item-1):
    print(i+1,'.  ',cart[i],'   ',list[cart[i]],'   ',item_quantity[i],
         '    = ',item_quantity[i]*list[cart[i]])


print()
print(' '*15,"total bill = ",bill,' '*4)
print('-'*30)
print('thank u visit again  :)')
print('\n\n')

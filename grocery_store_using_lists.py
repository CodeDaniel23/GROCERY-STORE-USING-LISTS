products=['Milk', 'Bread', 'Cheese', 'Flour packet','Biscuets', 'Crunchy pops', 'Btea', 'Gtea','Cream-bread','Borbun']
prices=[2.5, 3.0,4.0,6.3,2.0,1.5,5.0,5.3,1.8,2.7]
stocks=[5,6,3,7,5,4,3,2,8,10]
'''
print(len(products))
print(len(prices))
print(len(stocks))'''

def display_(inp):
    global products, prices, stocks
    if inp.lower()=='yes':
        print('='*50)
        print(f" {'GROCERY STORE INVENTORY' : ^50} ")
        print('='*50)
        print(f"| {'product': ^20} | {'prices($)': ^10} | {'stocks': ^10} |")
        print('-'*50)
        for i in range (len(products)):
            print(f"| {products[i]:<20} | {prices[i]:^10} | {stocks[i]:^10} |")
        print('-'*50)
    elif inp.lower()=='no':
        print('you can search one by one!')
        s=int(input('We have totally 10 items in store, you can check by giving any number b/w 1 to 10: '))
        if 1<=s<= len(products):
            s-=1
            print()
            print(f"{'PRODUCT DETAILS': ^45}")
            print('-'*45)
            print(f" {'Product': ^15}  {'Price($)': ^10}  {'Stocks':^10} ")
            print('-'*45)
            print(f" {products[s]:<15}  {prices[s]:^10}   {stocks[s]:^10}")
        else:
            print('Invalid number')
    else:
        print('Invalid answer')

def update_price(product_name, new_price):
    global products, prices
    if product_name in products:
        index=products.index(product_name)
        prices[index]=new_price
    return product_name, new_price
product_name='Milk'
new_price=2.8
product, price=update_price(product_name, new_price)
#print(product, price)

def stock_update(g_tea, upd_stock):
    global products, stocks
    if g_tea in products:
        index=products.index(g_tea)
        stocks[index]= upd_stock
    return g_tea, upd_stock
g_tea= 'Gtea'
upd_stock= 8
green_tea, greentea_stock=stock_update(g_tea,upd_stock)
#print(green_tea, greentea_stock)

def update_product(che_see ):
    global products, prices, stocks  
    if che_see in products:
        index=products.index(che_see)
        products.pop(index)
        prices.pop(index)
        stocks.pop(index)
        return products
    else:
        print(f'product not found')
x= 'Cheese'
ch=update_product(x)
#print(ch)

print(f"Updated price of Milk is {new_price}")
print(f"Updated stocks of Gtea are {upd_stock}")
print("Product Chesee is completed, we 'sorry' for the inconvinence we had today.")
print()
x=input('Do you want to check out the list of groceries yes/ no: ');print()
display_(x)
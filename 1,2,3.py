import pandas as pd
import numpy as np

#read data frame
df = pd.read_csv('Online Retail.csv',encoding= 'unicode_escape')

#1)number_of_transaction

number_of_transaction = len(set(list(df['InvoiceNo'])))
print('number_of_transaction: ',number_of_transaction )


#2)sum_of_each-StockCode

#drop rows that have negative quantity
#df_without_negative= df.drop(df.index[df['Quantity'] < 0])
df = df.loc[df.Quantity>0]

#filter columns are needed
df = df.loc[:,['InvoiceNo','StockCode','Quantity','CustomerID']]

#gaining the list of stocks 
list_quantity=[]
list_of_stock =sorted(set(list(df['StockCode'])))

#gaining the quantity of each stock 

list_of_stocksquantity=[]
for index in list_of_stock:
    quantity= np.sum(df.loc[df.StockCode ==(index),'Quantity'])
    list_quantity.append(quantity)
#zipping the quantity to each stock 
    
zipping_quantity_stock = list(zip(list_of_stock, list_quantity))
print('zipping_quantity_stock: ', zipping_quantity_stock)



#3)number_of_customers

number_of_customers = len(set(list(df['CustomerID'])))
 
print('number_of_customers: ',number_of_customers)

import pandas as pd
import numpy as np


#read data frame

df = pd.read_csv('Online Retail.csv',encoding= 'unicode_escape')


#filter the df by two InvoiceNo and StockCode columns

df_InvoiceNo = df[['InvoiceNo','StockCode']]
#print(df_InvoiceNo)


#convert InvoiceNo column to list_InvoiceNo

list_InvoiceNo= list(set(list(df['InvoiceNo'])))


#convert StockCode column to list_StockCode based on InvoiceNo

list_StockCode = []
for element in list_InvoiceNo:
    data = df_InvoiceNo.loc[df_InvoiceNo.InvoiceNo == (element) ]
   # print('data',data)

    data2 = data['StockCode'].values.tolist()
    list_StockCode.append(data2)
   # print(data2)


#section 2
#count how many same stocks are inlist_StockCode based on len each stock
   
rank_list=[]
count_list=[]
list_state=[]

for second_object_index in list_StockCode:
    value= second_object_index
    list_value=[]
    
    if(len(value))==2:
        list_value= value
        list_state.append(list_value)

    elif (len(value))>2:
        for i in range (0,len(value)):
            for j in range(0,len(value)):
                if i!=j:
                    if[value[i],value[j]] not in list_value:
                        if [value[j],value[i]] not in list_value:

                            list_value.append([value[i],value[j]])
        list_state.extend(list_value)
    
    
#remove elements that are duplicated 
        
list_uptimized=[]
for element in list_state:
    if element not in list_uptimized:
        list_uptimized.append(element)

list_counter=[]
for item in list_uptimized:
    item_reverse = item[::-1]
    counter= list_state.count(item) +  list_state.count(item_reverse)       
    list_counter.append(counter)


       
#zipping list_StockCode to count_list that shows the number of duplicated stock
zipped_stock_count = list(zip(list_uptimized, list_counter))
print('zipped_stock_count',zipped_stock_count)

# gaining the mean of stock's repetition 
sum_element=0
for element in (zipped_stock_count):
    sum_element += element[1]
    mean_element = np.ceil(sum_element/(len(zipped_stock_count)))
#print('mean_element',mean_element)


#filtering elements that the number of repetitions is lower than mean 
    
counter_high_list=[]
for element in zipped_stock_count:
    if element[1]>= int(mean_element):
        counter_high_list.append(element)
#print('counter_high_list',counter_high_list)

#remove elements that are duplicated 
        
result_list=[]
for element in counter_high_list:
    temp=element[0]
    element_reverse = temp[::-1]
    element_reserved=(element_reverse,element[1] )
    print('element_reserved',element_reserved)
    if element not in result_list:
        if element_reserved not in result_list:
            result_list.append(element)

        
print('list of products that are most sold together: ',result_list)

#gaining the products are most sold together  
     
num=(0,0)
for element in result_list:
    if element[1]>num[1]:
        num = element

print('products are most sold together : ',num)




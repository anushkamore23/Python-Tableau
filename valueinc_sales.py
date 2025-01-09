# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:45:01 2024

@author: Anushka
"""

import pandas as pd
# file_name = pd.read_csv('file.csv')
data =  pd.read_csv('transaction.csv')
data =  pd.read_csv('transaction.csv',sep=';')

# summary of the data
data.info()

# defining variables
CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Working with calculations on Tableau

ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellinPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

#variable = dataframe['column_name'] ->> To singleout a column

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# Add column into dataframe (method 1)

data['CostPerTransaction'] = CostPerTransaction

#Add column into dataframe (method 2)

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction'] 

# Markup = (sales-cost)/cost 

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

# rounding up markup

roundmarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

# Combining data feilds

my_date = 'Day' + '-' + 'Month' + '-' + 'Year'

# checking columns data type

print(data['Day'].dtype)

# changing data type

day = data['Day'].astype(str)
print(day.dtype)

year = data['Year'].astype(str)
print(year.dtype)

my_date = day +'-'+ data['Month'] +'-'+ year

data['date'] = my_date

# using iloc to view specific rows/columns

data.iloc[0] 
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows
data.head(5)   #first 5 rows
data.iloc[:,2] #all rows in 2nd column
data.iloc[4,2] #4th row 2nd column

# using split to split client keyword feild
# new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

# creating new columns for the split columns in the ClientKeywords

data['ClientAge'] = split_col[0] 
data['ClientType'] = split_col[1] 
data['LengthOfContract'] = split_col[2]

# using the replace function 
data['ClientAge'] = data['ClientAge'].str.replace('[','') 
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','') 

# using lower function to change the item to lowercase 

data['ItemDescription'] = data['ItemDescription'].str.lower() 

data['ItemDescription'] = data['ItemDescription'].str.upper()

# how to merge files
# bringing in new data set 

seasons =  pd.read_csv('value_inc_seasons.csv',sep=';')

# merging files: merge_df = pd.merge(old_df,new_df, on = 'key') 
data = pd.merge(data, seasons, on ='Month') 

# dropping columns
# df = df.drop('column name', axis=1)
data = data.drop('ClientKeywords', axis=1) 
data = data.drop('Day', axis=1)
data = data.drop(['Year','Month'], axis=1)

# export to csv
data.to_csv('ValueInc_Cleaned.csv' , index= False)























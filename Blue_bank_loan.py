import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#method 1 to read json file
json_file = open('loan_data_json.json') 
data = json.load(json_file)

#method 2 to read json file
with open('loan_data_json.json') as json_file:
  data = json.load(json_file)  

# tranform into dataframe 

loan_data = pd.DataFrame(data) 

loan_data.info()

# finding unique values from the purpose column

loan_data['purpose'].unique()

# describe the data 
loan_data.describe() 

# describe the data for a specific column 
loan_data['int.rate'].describe() 
loan_data['fico'].describe() 
loan_data['dti'].describe() 

# using exp() to get the actual annual income

income = np.exp(loan_data['log.annual.inc']) 
loan_data['annualincome'] = income 

# fico score

fico = 200 

if fico >= 300 and fico < 400:
    ficocat = 'Very poor' 
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'   
elif fico >= 600 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent' 
else:
    ficocat = 'Unknown' 
    
print(ficocat)    

# using range 0-10
length = len(loan_data)
ficocat = []
for x in range(0, length):
    category = loan_data['fico'][x] 
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very poor'
        elif category >= 400 and category < 600:
            cat = 'Poor' 
        elif category >= 600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'    
        elif category >= 700: 
            cat = 'Excellent' 
        else:
            cat = 'Unknown' 
    except:
        cat = 'Error'
        
    ficocat.append(cat) 
    
ficocat = pd.Series(ficocat)    
loan_data['fico.category'] = ficocat
   
    
# testing try and except 
# length = len(loan_data)
# ficocat = []
# for x in range(0, length):
#     category = 'red' 
#     try:
#         if category >= 300 and category < 400:
#             cat = 'Very poor'
#         elif category >= 400 and category < 600:
#             cat = 'Poor' 
#         elif category >= 600 and category < 660:
#             cat = 'Fair'
#         elif category >= 660 and category < 700:
#             cat = 'Good'    
#         elif category >= 700: 
#             cat = 'Excellent' 
#         else:
#             cat = 'Unknown' 
#     except:
#         cat = 'Error'
#     ficocat.append(cat)

# df.loc as conditional statements
# df.loc[[columnname] condition, new columnname] = 'value if the condition satisfies

# for interest rates new column is needed. if rate >0.12 then high else low 
loan_data.loc[loan_data['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loan_data.loc[loan_data['int.rate'] <= 0.12, 'int.rate.type'] = 'Low' 

# number of loans?rows from fico.category 

catplot = loan_data.groupby(['fico.category']).size() 
catplot.plot.bar(color = 'green', width = 0.2) 
plt.show()
purposecount = loan_data.groupby(['purpose']).size()
purposecount.plot.bar(color = 'pink', width = 0.2) 
plt.show() 

# scatter plots 
ypoint = loan_data['annualincome'] 
xpoint = loan_data['dti'] 
plt.scatter(xpoint,ypoint) 
plt.show() 

# writing to csv 

loan_data.to_csv('loan_cleaned.csv', index='True')









 

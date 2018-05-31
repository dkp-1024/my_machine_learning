import pandas as pd 

#create another data with duplicated rows
data = pd.DataFrame({'k1':['one']*3 + ['two']*4, 'k2':[3,2,1,3,3,4,4]})
print(data)

#sort values 
data.sort_values(by='k2')

#remove duplicates - ta da! 
data.drop_duplicates()

# Here, we removed duplicates based on matching row values across all columns. 
# Alternatively, we can also remove duplicates based on a particular column. 
# Let's remove duplicate values from the k1 column.

data.drop_duplicates(subset='k1')

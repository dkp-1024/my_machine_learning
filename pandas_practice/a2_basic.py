import pandas as pd 
#Let's create another data frame.
data = pd.DataFrame({'group':['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

#Let's sort the data frame by ounces - inplace = True will make changes to the data
data.sort_values(by=['ounces'],ascending=True,inplace=False)
print(data)

# sorting by multiple columns
data.sort_values(by=['group','ounces'],ascending=[True,False],inplace=False)
print(data)



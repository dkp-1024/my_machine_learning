#load library - pd is just an alias. I used pd because it's short and literally abbreviates pandas.
#You can use any name as an alias. 
import pandas as pd

#create a data frame - dictionary is used here where keys get converted to column names and values to row values.
data = pd.DataFrame({'Country': ['Russia','Colombia','Chile','Equador','Nigeria'],
                    'Rank':[121,40,100,130,11]})
print(data)
print(data.describe())
print(data.info())

import pandas as pd

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'], 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

# we want to create a new variable which indicates the type of animal which acts as the source of the food

# To do that, first we'll create a dictionary to map the food to the animals. 
# Then, we'll use map function to map the dictionary's values to the keys. 
# Let's see how is it done.

meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}

def meat_2_animal(series):
    if series['food'] == 'bacon':
        return 'pig'
    elif series['food'] == 'pulled pork':
        return 'pig'
    elif series['food'] == 'pastrami':
        return 'cow'
    elif series['food'] == 'corned beef':
        return 'cow'
    elif series['food'] == 'honey ham':
        return 'pig'
    else:
        return 'salmon'

#create a new variable
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print(data)

#another way of doing it is: convert the food values to the lower case and apply the function
lower = lambda x: x.lower()
data['food'] = data['food'].apply(lower)
data['animal2'] = data.apply(meat_2_animal, axis='columns')
print(data)

'''
# here, the entire data frame 'data' is dropped
data.drop(data.index, inplace=True)
# df.iloc[0:0]
'''

'''
Another way to create a new variable is by using the assign function. 
With this tutorial, as you keep discovering the new functions, you'll realize how powerful pandas is.
'''

data.assign(new_variable = data['ounces']*10)

print(data)
import numpy as np
import pandas as pd
import tensorflow as tf 
# from sklearn import preprocessing
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

def check_the_data():
	#check data set
	print(train.info())
	print ("The train data has",train.shape)
	print ("The test data has",test.shape)
	# ('The train data has', (32561, 15))
	# ('The test data has', (16281, 15))
	#Let have a glimpse of the data set
	print(train.head())	

def check_for_missing_values():
	nans = train.shape[0] - train.dropna().shape[0]
	print ("%d rows have missing values in the train data" %nans)

	nand = test.shape[0] - test.dropna().shape[0]
	print ("%d rows have missing values in the test data" %nand)

	# We should be more curious to know which columns have missing values.
	#only 3 columns have missing values
	train.isnull().sum()
	print(train.isnull().sum())	

def count_unique_values():
	cat = train.select_dtypes(include=['O'])
	print(cat.apply(pd.Series.nunique))

def impute_missing():
	#Education
	train.workclass.value_counts(sort=True)
	train.workclass.fillna('Private',inplace=True)

	#Occupation
	train.occupation.value_counts(sort=True)
	train.occupation.fillna('Prof-specialty',inplace=True)

	#Native Country
	train['native.country'].value_counts(sort=True)
	train['native.country'].fillna('United-States',inplace=True)

def check_balance():
	#check proportion of target variable
	print(train.target.value_counts()/train.shape[0])
	'''
	We see that 75% of the data set belongs to <=50K class. 
	This means that even if we take a rough guess of target prediction as <=50K, we'll get 75% accuracy. 
	Isn't that amazing? Let's create a cross tab of the target variable with education. 
	With this, we'll try to understand the influence of education on the target variable.
	'''
	print(pd.crosstab(train.education, train.target,margins=True)/train.shape[0])
	# print("We see that out of 75% people with <=50K salary, 27% people are high school graduates, which is correct as people with lower levels of education are expected to earn less. On the other hand, out of 25% people with >=50K salary, 6% are bachelors and 5% are high-school grads. Now, this pattern seems to be a matter of concern. That's why we'll have to consider more variables before coming to a conclusion.")

#......................................................load the data
train  = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# check_the_data()

check_for_missing_values()

'''
Let's count the number of unique values from character variables.
'''
count_unique_values()
impute_missing()
check_for_missing_values()
check_balance()

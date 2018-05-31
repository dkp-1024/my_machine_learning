#Let's load the data set and do initial data analysis:


#set working directory
# path <- "C:/Users/Data/UCI"
# setwd(path)
# no need


#load data and check data
mydata <- read.csv("airfoil_self_noise.csv")
str(mydata)

# This data has 5 independent variables and Sound_pressure_level as the dependent variable (to be predicted). 
# In predictive modeling, we should always check missing values in data. 
# If any data is missing, we can use methods like mean, median, and predictive modeling imputation to make up for missing data.

#check missing values
colSums(is.na(mydata))
# This data set has no missing values. Good for us! Now, to avoid multicollinearity, let's check correlation matrix.
cor(mydata)

# After you see carefully, you'd infer that Angle_of_Attack and Displacement show 75% correlation. 
# It's up to us if we should consider this correlation % as a damaging level. 
# Usually, correlation above 80% (subjective) is considered higher. 
# Therefore, we can forego this combination and won't remove any variable.

# In R, the base function lm is used for regression. We can run regression on this data by
regmodel <- lm(Sound_pressure_level ~ ., data = mydata)
summary(regmodel)

# ~ . tells lm to use all the independent variables. Let's understand the regression output in detail:

# The adjusted R² implies that our model explains ~51% total variance in the data. 
# And, the overall p value of the model is significant. 
# Can we still improve this model ? Let's try to do it. 
# Now, we'll check the residual plots, understand the pattern and derive actionable insights (if any):
#set graphic output
par(mfrow=c(2,2))
#create residual plots
plot (regmodel)

# Among all, Residual vs. Fitted value catches my attention. 
# Not exactly though, but I see signs of heteroskedasticity in this data. 
# Remember funnel shape? You can see a similar pattern. 
# To overcome this situation, we'll build another model with log(y).
# # To overcome this situation, we'll build another model with log(y).
regmodel <- update(regmodel, log(Sound_pressure_level)~.)
summary(regmodel)

# Though, the improvement isn't significant, we've increased our adjusted R² to 52.19%. 
# Also, it looked like that funnel shape wasn't completely evident, thus implying non-severe effect of non-constant variance.
# Let's divide the data set into train and test to check our final evaluation metric. 
# We'll keep 70% data in train and 30% in test file. 
# The reason being that we should keep enough data in train so that the model identifies obvious emerging patterns.

#sample
set.seed(1)
d <- sample ( x = nrow(mydata), size = nrow(mydata)*0.7)
train <- mydata[d,] #1052 rows 
test <- mydata[-d,] #451 rows

#train model
regmodel <- lm (log(Sound_pressure_level)~.,data = train)
summary(regmodel)

#test model
regpred <- predict(regmodel, test)

#convert back to original value
regpred <- exp(regpred)

library(Metrics)
rmse(actual = test$Sound_pressure_level,predicted = regpred)
# [1] 5.03423

# Interpretation of RMSE error will be more helpful while comparing it with other models. 
# Right now, we can't say if 5.03 error is the optimal value we could expect. 
# I've got you started solving regression problems. 
# Now, you should spend more time and try to obtain a lower error rate than 5.03. 
# For example, you should next check for outlier values using a box plot:
#save the output of boxplot
d <- boxplot(train$Displacement,varwidth = T,outline = T,border = T,plot = T)
d$out #enlist outlier observations


# Refer to googleplaystore.csv file and solve following questions
#     a. Display First 5 records from Dataframe.
#     b. Display category with highest number of apps registered.
#     c. What is the average rating for all the apps
#     d. Display total number of apps which even supports Andriod version 2.3 and up
#     e. Impute the missing values available in rating column with respective measure
#     of central tendency.


import pandas as pd 

df = pd.read_csv('D:\dataset\googleplaystore.csv')

# a. Display First 5 records from Dataframe.
print(df.head())

# b. Display category with highest number of apps registered.
result = df['Category'].value_counts()

print('Category with highest number of app registered :', result.idxmax())
print('Number of App :' , result.max())


# c. What is the average rating for all the apps

avg = df['Rating'].mean()
print('Average of Rating :', avg)


# d. Display total number of apps which even supports Andriod version 2.3 and up

count = (df['Android Ver'] == '2.3 and up').sum()

print("Total number of apps :" , count)


# e. Impute the missing values available in rating column with respective measure
#     of central tendency.

df['Rating'].isnull().sum()

median_rating = df['Rating'].median()

df['Rating'] = df['Rating'].fillna(median_rating)

print("Missing values after imputation :" , df['Rating'].isnull().sum())
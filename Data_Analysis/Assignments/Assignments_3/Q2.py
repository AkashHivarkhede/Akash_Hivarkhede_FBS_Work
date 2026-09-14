# Refer to salaries.xlsx file and solve following questions
#     a. Check head of the dataframe
#     b. Find out details about no. of entries & no. of columns in the data frame
#     c. What is the average base pay?
#     d. What is the highest amount of overtime pay in the dataset?
#     e. What is the job title of JOSEPH DRISCOLL?
#     f. How much does JOSEPH DRISCOLL make (including benefits)?
#     g. How many unique job titles are there?
#     h. What are the top 5 common jobs?


import pandas as pd

df = pd.read_excel('D:\Dataset\Salaries.xlsx')

# a. Check head of the dataframe
print(df.head())

# b. Find out details about no. of entries & no. of columns in the data frame
print('Number of entries :',df.shape[0])
print('Number of columns :',df.shape[1])

# c. What is the average base pay?
Avg_base_pay = df['BasePay'].mean()
print('Average of Base pay :', Avg_base_pay)

#  d. What is the highest amount of overtime pay in the dataset?
high_overtime_pay = df['OvertimePay'].max()
print('Higest Overtime Pay :', high_overtime_pay)

# e. What is the job title of JOSEPH DRISCOLL?
employee = df[df['EmployeeName'] == 'JOSEPH DRISCOLL']
print('Job Title of JOSEPH DRISCOLL :' , employee['JobTitle'].values[0])

# f. How much does JOSEPH DRISCOLL make (including benefits)?
print('JOSEPH DRISCOLL Total Pay Including Benefits:',employee['TotalPayBenefits'].values[0])

# g. How many unique job titles are there?
unique_jobs  = df['JobTitle'].nunique()
print('Number of unique job titles :',unique_jobs )

# h. What are the top 5 common jobs?
top_5_jobs = df['JobTitle'].value_counts().head()
print('Top 5 common jobs :')
print(top_5_jobs)
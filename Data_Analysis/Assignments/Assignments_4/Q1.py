# Dataset: Consider the following dataset of sales records:

# OrderID   Customer    Product   Category    Quantity    Price   TotalSales
# 1001     Alice         Laptop   Electronics     2       800       1600
# 1002     Bob           Phone    Electronics     1       500       500
# 1003     Charlie       Chair    Furniture       4       100       400
# 1004     Alice         Table    Furniture       1       250       250
# 1005     David         Laptop   Electronics     1       800       800
# 1006     Charlie       Phone    Electronics     2       500       1000
# 1007     Bob           Chair    Furniture       2       100       200
# 1008     Alice         Phone    Electronics     1       500       5000


# Tasks:
# 1. Create a DataFrame:
#   o Load the above dataset into a Pandas DataFrame.

# 2. Add a New Column:
#   o Add a column Discount that gives a 10% discount on total
#     sales.

# 3. Add a New Row:
#   o Add a new sales record: Order ID = 1009, Customer =
#       "Eve", Product = "Tablet", Category = "Electronics",
#       Quantity = 1, Price = 300, Total Sales = 300.

# 4. Filter Data:
#   o Retrieve only the sales records where the Category is
#       "Electronics".

# 5. Selection:
#   o Select the Customer and Total Sales columns.

# 6. Grouping:
#   o Group the data by Customer and calculate the total sales per customer.

# 7. Sorting:
#    o Sort the DataFrame based on Total Sales in descending
#      order.

# 8. Apply Function:
#   o Apply a lambda function to create a new column Sales
#       Category, where values are labeled as "High" if Total Sales >'
#       1000, otherwise "Low".

# 9. Save DataFrame:
#   o Save the final DataFrame as a CSV file named sales_data.csv.


import pandas as pd

# 1. Create a DataFrame:
#   o Load the above dataset into a Pandas DataFrame.


data = {
    "Order Id" : [1001 , 1002 , 1003 , 1004 , 1005 , 1006 , 1007 , 1008],
    "Customer" : ["Alice", "Bob", "Charlie", "Alice", "David", "Charlie", "Bob", "Alice"],
    "Products" : ["Laptop" , "Phone" , "Chair" , "Table" , "Laptop" , "Phone" , "Chair" , "Phone"],
    "Category": ["Electronics", "Electronics", "Furniture", "Furniture",
                 "Electronics", "Electronics", "Furniture", "Electronics"],
    "Quantity": [2, 1, 4, 1, 1, 2, 2, 1],
    "Price": [800, 500, 100, 250, 800, 500, 100, 500],
    "Total Sales": [1600, 500, 400, 250, 800, 1000, 200, 500]
}

df = pd.DataFrame(data)

print("DataFrame")
print(df)

# 2. Add a New Column:
#   o Add a column Discount that gives a 10% discount on total sales.

df['Discount'] = df['Total Sales'] * 0.10
print('\nAdding after Discount :')
print(df)

# 3. Add a New Row:
#   o Add a new sales record: Order ID = 1009, Customer =
#       "Eve", Product = "Tablet", Category = "Electronics",
#       Quantity = 1, Price = 300, Total Sales = 300.

new_row = {

    "Order Id" : 1009,
    "Customer" : "Eve",
    "Products"  : "Table",
    "Category" : "Electronics",
    "Quantity" : 1,
    "Price"    : 300 ,
    "Total Sales" : 300,
    "Discount" : 300 * 0.10

}

df.loc[len(df)] = new_row   

print("\nDataFrame after adding new row :")
print(df)


# 4. Filter Data:
#   o Retrieve only the sales records where the Category is "Electronics".


electronics = df[df['Category'] == "Electronics"]
print('\n Electronics')
print(electronics)


# 5. Selection:
#   o Select the Customer and Total Sales columns.

selected_columns = df[['Customer','Total Sales']]
print('\nCustomer and Total Sales')
print(selected_columns)


# 6. Grouping:
#   o Group the data by Customer and calculate the total sales per customer.

customer_sales = df.groupby('Customer')['Total Sales'].sum()
print('\n Total sales per Customer:')
print(customer_sales)



# 7. Sorting:
#    o Sort the DataFrame based on Total Sales in descending order.

sorted_df = df.sort_values('Total Sales', ascending=False)
print('\nDataFrame sorted by total sales :')
print(sorted_df)



# 8. Apply Function:
#   o Apply a lambda function to create a new column Sales
#       Category, where values are labeled as "High" if Total Sales >'
#       1000, otherwise "Low".

df['Sales Category'] = df['Total Sales'].apply(
    lambda x: "High" if x > 1000 else "Low"
)

print("\nDataFrame with Sales Category:")
print(df)

# 9. Save DataFrame:
#   o Save the final DataFrame as a CSV file named sales_data.csv.

df.to_csv('sales_data.csv' , index=False)

print("\nFinal DataFrame saved as sales_data.csv")
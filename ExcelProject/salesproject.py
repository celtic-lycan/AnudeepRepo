# Import necessary Python libraries
import numpy as np            # NumPy is used for numerical operations on arrays.
import pandas as pd           # Pandas is used for data manipulation and analysis.
import matplotlib.pyplot as plt # Matplotlib is used for plotting and visualizing data.
df = pd.read_csv('SuperMart.csv', encoding='unicode_escape') # Reads the CSV file and loads it into a DataFrame `df`. The encoding is specified to handle special characters.

# Show the shape of the DataFrame (rows, columns)
df.shape  # Returns the number of rows and columns in the DataFrame.

# Show the first few rows of the DataFrame
df.head()  # Displays the first five rows of the DataFrame.

# Display information about the DataFrame
df.info()  # Provides a summary of the DataFrame, including data types, non-null counts, and memory usage.

# Drop unrelated or blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True) # Removes the 'Status' and 'unnamed1' columns from the DataFrame.

# Check for null values in each column
pd.isnull(df).sum()  # Returns the count of null (missing) values in each column of the DataFrame.

# Drop rows with null values
df.dropna(inplace=True)  # Removes any rows with missing values from the DataFrame.

# Change the data type of the 'Amount' column to integer
df['Amount'] = df['Amount'].astype('int')  # Converts the 'Amount' column to integer type.

# Verify the data type of the 'Amount' column
df['Amount'].dtypes  # Returns the data type of the 'Amount' column.

# Show the names of all columns
df.columns  # Lists all the column names in the DataFrame.

# Rename a column
df.rename(columns={'Marital_Status': 'Shaadi'})  # Renames the 'Marital_Status' column to 'Shaadi'.

# Generate descriptive statistics for the DataFrame
df.describe()  # Returns summary statistics of the DataFrame, such as count, mean, standard deviation, etc.

# Generate descriptive statistics for specific columns
df[['Age', 'Orders', 'Amount']].describe()  # Returns summary statistics for the 'Age', 'Orders', and 'Amount' columns.

# Plot a bar chart for Gender and its count
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(7, 5))
ax = gender_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Count')
ax.bar_label(ax.containers[0])
plt.show()

# Plot a bar chart for Gender vs Total Amount
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(7, 5))
plt.bar(sales_gen['Gender'], sales_gen['Amount'], color='skyblue')
plt.xlabel('Gender')
plt.ylabel('Total Amount')
plt.title('Gender vs Total Amount')
plt.show()

# Plot a bar chart for Age Group vs Gender
age_gender_counts = df.groupby(['Age Group', 'Gender']).size().unstack(fill_value=0)
ax = age_gender_counts.plot(kind='bar', stacked=True, figsize=(10, 6), color=['skyblue', 'lightgreen'])
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Age Group vs Gender')
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.show()

# Plot Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(7, 5))
plt.bar(sales_age['Age Group'], sales_age['Amount'], color='skyblue')
plt.xlabel('Age Group')
plt.ylabel('Total Amount')
plt.title('Age Group vs Total Amount')
plt.show()

# Plot the total number of orders from the top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
plt.figure(figsize=(15, 5))
plt.bar(sales_state['State'], sales_state['Orders'], color='skyblue')
plt.xlabel('State')
plt.ylabel('Number of Orders')
plt.title('Top 10 States by Number of Orders')
plt.show()

# Plot the total amount/sales from the top 10 states
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
plt.figure(figsize=(15, 5))
plt.bar(sales_state['State'], sales_state['Amount'], color='skyblue')
plt.xlabel('State')
plt.ylabel('Total Amount')
plt.title('Top 10 States by Total Amount')
plt.show()

# Plot a count of Marital Status
marital_status_counts = df['Marital_Status'].value_counts()
plt.figure(figsize=(7, 5))
ax = marital_status_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.title('Marital Status Count')
ax.bar_label(ax.containers[0])
plt.show()

# Plot a count of Occupation
occupation_counts = df['Occupation'].value_counts()
plt.figure(figsize=(20, 5))
ax = occupation_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.title('Occupation Count')
ax.bar_label(ax.containers[0])
plt.show()

# Plot the total sales amount by occupation
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(20, 5))
plt.bar(sales_state['Occupation'], sales_state['Amount'], color='skyblue')
plt.xlabel('Occupation')
plt.ylabel('Total Amount')
plt.title('Total Amount by Occupation')
plt.show()

# Plot a count of Product Categories
product_category_counts = df['Product_Category'].value_counts()
plt.figure(figsize=(20, 5))
ax = product_category_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Product Category')
plt.ylabel('Count')
plt.title('Product Category Count')
ax.bar_label(ax.containers[0])
plt.show()

# Plot the total sales amount by product category
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
plt.figure(figsize=(20, 5))
plt.bar(sales_state['Product_Category'], sales_state['Amount'], color='skyblue')
plt.xlabel('Product Category')
plt.ylabel('Total Amount')
plt.title('Top 10 Product Categories by Total Amount')
plt.show()

# Plot the top 10 most ordered products
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
plt.figure(figsize=(20, 5))
plt.bar(sales_state['Product_ID'], sales_state['Orders'], color='skyblue')
plt.xlabel('Product ID')
plt.ylabel('Number of Orders')
plt.title('Top 10 Most Ordered Products')
plt.show()

# Plot the top 10 most sold products (same thing as above)
plt.figure(figsize=(12, 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.xlabel('Product ID')
plt.ylabel('Number of Orders')
plt.title('Top 10 Most Sold Products')
plt.show()

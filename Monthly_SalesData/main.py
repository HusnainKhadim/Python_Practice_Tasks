# Importing Pandas
import pandas as pd

# Reading csv file
df = pd.read_csv('BehbudBoutique_RawData_Sample.csv')

# Adding Month column
df['Month'] = df['Created Date'].str[3:5]

# Changing the type of Month
df['Month'] = df['Month'].astype('int32')

# Adding Sales column
df['Sales'] = df['Quantity']*df['Price']

# Fetching the record of specific month
month = int(input("Enter the number of month to get its record: "))
month_wise_records = df.loc[df['Month'] == month]

# Dropping all the null rows
month_wise_records=month_wise_records.dropna(how='all')

# Re-ordering the month column
columns = ['Month'] + [col for col in month_wise_records.columns if col != 'Month']
month_wise_records = month_wise_records[columns]

# Creating a new csv file
month_wise_records.to_csv('Month Wise Records.csv', index=False)

print(f"A seperate file of the {month}th month records is created!")


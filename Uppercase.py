import pandas as pd

# Reading csv file
df = pd.read_csv('/home/husnain/Desktop/BehbudBoutique_RawData_Sample.csv')
# Uppercasing the name
df['Billing Name'] = df['Billing Name'].str.upper()
# Creating a new csv file
df.to_csv('UpperCase.csv', index=False)
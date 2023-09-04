import pandas as pd
# Read csv file
df = pd.read_csv('/home/husnain/Desktop/BehbudBoutique_RawData_Sample.csv')
# Converting string into datetime
df['Created Date'] = pd.to_datetime(df['Created Date'], dayfirst=True)
# Creating a new file
df.to_csv('Proper Date', index=False)

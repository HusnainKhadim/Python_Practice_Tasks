#Importing modules
import pandas as pd
import re

# Reges expression
regex = re.compile(r'^\d{5}-\d{7}-\d$')

# Function to validate cnic
def validate_cinc(cnic):
    if re.fullmatch(regex,str(cnic)):
        return cnic
    else:
        return None

# Creating dataframe and apllying 
df = pd.read_csv('/home/husnain/Desktop/BehbudBoutique_RawData_Sample.csv')
df['Cnic'] = df['Cnic'].apply(validate_cinc)
df.to_csv('Validated_cnic.csv', index=False)

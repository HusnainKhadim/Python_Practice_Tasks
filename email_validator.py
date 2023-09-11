# Importing modules
import pandas as pd
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+') 

def emailValid(email):
    if re.fullmatch(regex,str(email)):
        return email
    else:
        return None

df = pd.read_csv('/home/husnain/Desktop/BehbudBoutique_RawData_Sample.csv')
df['Email'] = df['Email'].apply(emailValid)
df.to_csv('Validted Emails.csv', index=False)
import pandas as pd
import re

regex = "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$";
validator = re.compile(regex)

def ssn_validator(expression):
    if re.fullmatch(regex, str(expression)):
        return expression
    else:
        return None


if __name__ == '__main__':

    df = pd.read_csv('/home/husnain/Desktop/BehbudBoutique_RawData_Sample.csv')
    df['SSN'] = df['SSN'].apply(ssn_validator)
    df.to_csv("SSN_Validated.csv", index=False)
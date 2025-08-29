import re
import sys
import pandas as pd

def fix_locations(df):
        pattern = r'^[0-9]+\s+locations,*'
        for i in range(len(df['location'])):
            fix = re.sub(pattern, '', df['location'][i])
            df.loc[i, 'location'] = fix
        return df

def fix_nan(df):
    #df.to_csv(index=False)

    return df

def fix_arrow(df):
    companies = []

    for i in range(len(df['company'])):
        if df['company'][i] != '↳':
            companies.append(df['company'][i])
        else:
            df.loc[i, 'company'] = companies[-1]
    return df
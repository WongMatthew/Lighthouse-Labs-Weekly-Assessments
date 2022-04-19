import pandas as pd
import sys
from supporting_files.data_loader import load_excel

df = load_excel('supporting_files/SaleData.xlsx')


"""
Write a function to count the manager wise sale (sale_cnt)
and mean value of sale amount (sale_mean). 
Order the output dataframe by sale_cnt, starting with the highest.
Output should be DataFrame with 3 columns (order is important):
    - Manager
    - sale_cnt
    - sale_mean
and numeric index starting with 0 (after sorting).
"""

def compute_agg_stats(df):
    columns = df[['Manager','Sale_amt']] 
    new_df = columns.copy()
    new_df = new_df.groupby(['Manager']).mean()
    new_df['sale_cnt'] = df['Manager'].value_counts()
    new_df = new_df.sort_values(by='sale_cnt', ascending=False)
    new_df = new_df.reset_index()
    new_df = new_df[["Manager", "sale_cnt", "Sale_amt"]]
    new_df = new_df.rename(columns={'Sale_amt': "sale_mean"})
    print(new_df)
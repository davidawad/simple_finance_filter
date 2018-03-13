import pandas as pd
import csv


f=pd.read_csv("input.csv")

total_columns = ['Date', 'Recorded at', 'Scheduled for', 'Amount', 'Activity', 'Pending', 'Raw description']

filtered_columns = ['Date', 'Amount', 'Description', 'Category']

# we only want the negative numbers, we only care about the money going outwards
f = f[filtered_columns].query('Amount < 0')

# take the money we've spent and convert it to positive money
f['Amount'] = f['Amount'].abs()

#  import pdb; pdb.set_trace()

#  new_f = f[keep_col]
f.to_csv("output.csv", index=False)


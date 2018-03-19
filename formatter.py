import pandas as pd
import csv


f=pd.read_csv("input.csv")

# these are the columns that the native simple CSV export uses
total_columns = ['Date', 'Recorded at', 'Scheduled for', 'Amount', 'Activity', 'Pending', 'Raw description']

# these are the columns I use in my spreadsheet
filtered_columns = ['Date', 'Amount', 'Description', 'Category']

# for me use case I only want the negative numbers. 
# I only want to know about money I'm spending. 
f = f[filtered_columns].query('Amount < 0')

# take the money we've spent and convert it to positive integers
f['Amount'] = f['Amount'].abs()

f.to_csv("output.csv", index=False)

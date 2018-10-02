import pandas as pd
import numpy as np
print(2*"\n"+60*"*"+"\n"+"Make sure everything is saved in a singel working directory"+"\n"+"e.g, save data file and gis_title_editor.py on Desktop"+"\n"+60*"*"+"\n")
x = input("Please type the original file name you wish to clean (in .csv format) and press enter: ")
y = input("\n"+"choose a name (in csv format) for the edited data file and press enter:")
print("Your file: " + x + " was cleaned"+"\n"+"check your desktop for "+y)

data = pd.read_csv(x,encoding = "ISO-8859-1")
first_row = data.iloc[0]

cols = []
for i in range(len(first_row)-1):
	title = first_row[i]
	if "Margin" in str(title):
		cols.append(i)
data.drop(data.columns[[cols]], axis=1, inplace=True)

data.columns = data.columns.str.replace(".", "_")
data.columns = data.columns.str.replace(",", "_")
data.columns = data.columns.str.replace(";", "_")
data.columns = data.columns.str.replace("-", "_")

for i, column in enumerate(data):
	
	if len(column)>10:
#         print(column[:9])
		data.columns.values[i] = column[:9]
    
	if column[0].isdigit():
		new_column = "_"+data.columns[i]
		data.columns.values[i] = new_column

data.to_csv(y, sep=',')

import pandas as pd
import os
import pickle

#We get the current working directory
current_path = os.path.abspath(os.getcwd())

#We store the name of the excel file we are going to read
excel_file_name = "data_example.xlsx"

#We join the current working directory path with the data folder in the repository
excel_file_path = os.path.join(current_path, "data")

#We build the complete path to the file
excel_file_path = os.path.join(excel_file_path, excel_file_name)

#We store the excel file on a variable we will access later
excel = pd.ExcelFile(excel_file_path)

sheet_name = "1 week example"
df = excel.parse(sheet_name = sheet_name)
df = df.set_index('Day').transpose()


print(df)
# To print the headers
print(df.columns.values)
# We store the data as a dictionary
data_dict = df.to_dict()
print(data_dict)


# We store the data on a file to read it later
with open('data_dict.pickle', 'wb') as file:
    pickle.dump(data_dict, file)

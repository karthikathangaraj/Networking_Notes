# from openpyxl import load_workbook 
# wb = load_workbook("students.xlsx")
# sheet = wb.active 

# for row in sheet.iter_rows(values_only=True):
#     print(row)

import pandas as pd

df = pd.read_excel("students.xlsx")

print(df)
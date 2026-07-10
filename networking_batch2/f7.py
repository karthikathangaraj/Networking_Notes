from openpyxl import Workbook

# Create a workbook
wb = Workbook()

# Select the active sheet
sheet = wb.active

# Write headers
sheet["A1"] = "ID"
sheet["B1"] = "Name"
sheet["C1"] = "Marks"

# Write data
sheet["A2"] = 1
sheet["B2"] = "Karthika"
sheet["C2"] = 95

sheet["A3"] = 2
sheet["B3"] = "Karnika"
sheet["C3"] = 95


# Save the workbook
wb.save("students.xlsx")

print("Data written successfully!")
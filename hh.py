
import openpyxl

wer = openpyxl.load_workbook("C:/.idea/dsa.xlsx")
sheet = wer["as"]

sheet["b12"] = "ggg"

wer.save("C:/.idea/dsa.xlsx")
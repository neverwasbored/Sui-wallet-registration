import pandas as pd

with open('data.json', 'r', encoding='utf-8') as json_file:
    data = pd.read_json(json_file)

output_path = 'output.xlsx'
data.to_excel(output_path, index=False, engine='openpyxl')

import openpyxl as op

wb = op.load_workbook('planilha_devolucoes.xlsx')

planilha = wb['Planilha1']

print(planilha['A1'].value)
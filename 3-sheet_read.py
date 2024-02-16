from openpyxl import load_workbook

# 1 - Lê pasta de trabalho e planilha
wb = load_workbook("data/pivot_table.ods")
sheet = wb["Relatorio"]

# 2 - Acessando valor específico
print(sheet["A3"].value)
print(sheet["B3"].value)

# 3 - Itrando valores por meio de loop
for i in range(2, 6):
    ano = sheet["A%" % i].value
    am = sheet["B%" % i].value
    bt = sheet["C%" % i].value
    print("{0} o Aston martin vendeu{1} e o Bentle vendeu {2}".format(ano, am, bt))

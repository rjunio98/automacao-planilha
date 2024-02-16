import pandas as pd

data = pd.read_excel("data/VendaCarros.ods")

print(data)


print(data.head())

print(data.tail())

print(data["Fabricante"].value_counts())

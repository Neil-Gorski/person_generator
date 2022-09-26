import pandas as pd

citys = pd.DataFrame(pd.read_excel("./data/citys_poland.xlsx"))

for row in citys["województwo"]:
    x = row.split("-")
    c = "-".join([i.capitalize() for i in x])
    row = c

print(citys)


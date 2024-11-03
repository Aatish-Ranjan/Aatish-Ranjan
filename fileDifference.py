import pandas as pd
df1 = pd.read_excel("C:/Users/aatis/Downloads/testsheet1.xlsx.xls")
df2 = pd.read_excel("C:/Users/aatis/Downloads/testsheet2.xlsx.xls")
new1 = df1.compare(df2)
new1.to_excel("new1.xlsx")
print("filemade")

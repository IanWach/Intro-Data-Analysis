import pandas as pd

print("It's the First I thank God")

df = pd.read_excel('VAR.xlsx')
print (df)
print("This is the tail Data")
new_df = df.tail

print(new_df)
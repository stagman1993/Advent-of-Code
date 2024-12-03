import pandas as pd

file = "day1input.txt"

df = pd.read_csv(file, sep="   ")

for col in df:
    df[col] = df[col].sort_values(ascending=True, ignore_index=True)
    df['difference'] = ""
for row in df.iloc():
    val_1 = row['val 1']
    val_2 = row['val 2']
    difference = abs(val_1 - val_2)
    df.loc[row.name, 'difference'] = difference

print(df['difference'].sum())
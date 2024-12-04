import pandas as pd

file = "day 1 input.txt"

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

#Part 2 of day 1:
similarity_list = []
for value in df['val 1']:
    count_of_value = df['val 2'].tolist().count(value)
    similarity_score = value * count_of_value
    similarity_list.append(similarity_score)

print(sum(similarity_list))
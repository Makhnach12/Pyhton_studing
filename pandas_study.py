import pandas as pd
import numpy as np


# homework
# task 1
# df = pd.read_csv('StudentsPerformance.csv')

# task 2
# df["mean score"] = (df["math score"] + df["reading score"] + df["writing score"]) / 3
# print(df)

# task 3
# print(df['race/ethnicity'].value_counts())

# task 4
# arr = df['race/ethnicity'].unique()
# arr_group = df[df['race/ethnicity'] == 'group A']
# for group in arr:
#     arr_group = df[df['race/ethnicity'] == group]
#     print(f'In {group}', end=' ')
#     print(arr_group['parental level of education'].value_counts())
#     print(f'In {group}', end=' ')
#     print(arr_group['lunch'].value_counts())
#     print(f'In {group}', end=' ')
#     print(arr_group['test preparation course'].value_counts())

# task 5
# print(df[(df['lunch'] == 'standard') & (df['reading score'] < df['writing score']) & (df['reading score'] < df['math score'])])

# task 6
# arr_read_score = df['reading score'].values
# arr_writing_score = df['writing score'].values
# arr_math_score = df['math score'].values
# quant_read_score = np.quantile(arr_read_score, 0.25, axis=0)
# quant_writing_score = np.quantile(arr_writing_score, 0.25, axis=0)
# quant_math_score = np.quantile(arr_math_score, 0.25, axis=0)
# print(df[(df['gender'] == 'male') & ((df['reading score'] < quant_read_score) |
#          (df['math score'] < quant_math_score) | (df['writing score'] < quant_writing_score))])


# homework
def replace_letter_marks(df: pd.DataFrame):
    score = {'A': 100, 'B': 75, 'C': 50, 'D': 35, 'E': 25, 'F': 15}
    for letter in score.keys():
        for column in list(df.columns)[7:]:
            df[column] = df[column].replace(letter, str(score[letter]))


# 1 task
df = pd.read_csv('StudentsPerformanceV3.tsv', sep='\t')

# 2 task and 3 task
replace_letter_marks(df)
for column in list(df.columns)[7:]:
    df[column] = df[column].replace(np.NaN, '0')
for column in list(df.columns)[7:]:
    df[column] = df[column].astype('int')
for column in list(df.columns)[:7]:
    df[column] = df[column].replace(np.NaN, '-')

# 4 task
df = df.drop_duplicates()

# 5 task
df["mean score"] = (df["math score"] + df["reading score"] + df["writing score"]) / 3
# print(df)

# 6 task
print(df['race/ethnicity'].value_counts())

# 7 task
arr = df['race/ethnicity'].unique()
for group in arr:
    arr_group = df[df['race/ethnicity'] == group]
    print(f'In {group}', end=' ')
    print(arr_group['parental level of education'].value_counts())
    print(f'In {group}', end=' ')
    print(arr_group['lunch'].value_counts())
    print(f'In {group}', end=' ')
    print(arr_group['test preparation course'].value_counts())

# 8 task
print(df[(df['lunch'] == 'standard') & (df['reading score'] < df['writing score']) &
         (df['reading score'] < df['math score'])])

# 9 task
arr_read_score = df['reading score'].values
arr_writing_score = df['writing score'].values
arr_math_score = df['math score'].values
quant_read_score = np.quantile(arr_read_score, 0.25, axis=0)
quant_writing_score = np.quantile(arr_writing_score, 0.25, axis=0)
quant_math_score = np.quantile(arr_math_score, 0.25, axis=0)
print(df[(df['gender'] == 'male') & ((df['reading score'] < quant_read_score) |
                                     (df['math score'] < quant_math_score) |
                                     (df['writing score'] < quant_writing_score))])

import pandas as pd
pd.set_option('display.max_columns', 8)

dfs = dict()
for name in ["general", "prenatal", "sports"]:
    dfs[name] = pd.read_csv(f"test/{name}.csv")
    dfs[name].drop("Unnamed: 0", axis=1, inplace=True)
    dfs[name].rename(str.lower, axis='columns', inplace=True)
    dfs[name].columns.values[1] = 'gender'

df = (pd.concat(dfs, axis=0, ignore_index=True)
    .dropna(axis=0, how='all')
    .replace(['male', 'man'], 'm')
    .replace(['female', 'woman'], 'f')
    .fillna({'gender': 'f'})
    .fillna({'bmi': 0, 'diagnosis': 0, 'blood_test': 0, 'ecg': 0, 'ultrasound': 0, 'mri': 0, 'xray': 0, 'children': 0, 'months': 0}))
print(df.shape)
print(df.sample(n=20, random_state=30))

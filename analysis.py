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

n_hospitals = df.hospital.value_counts()
print(f"The answer to the 1st question is {n_hospitals.idxmax()}")

r_stomach = df[df.hospital == 'general'].diagnosis.value_counts()['stomach'] / n_hospitals['general']
print(f"The answer to the 2nd question is {round(r_stomach, 3)}")

r_disc = df[df.hospital == 'sports'].diagnosis.value_counts()['dislocation'] / n_hospitals['sports']
print(f"The answer to the 3rd question is {round(r_disc, 3)}")

df_wide = df.pivot_table(columns='hospital', aggfunc='median')
diff = df_wide.loc['age', 'general'] - df_wide.loc['age', 'sports']
print(f"The answer to the 4th question is {diff}")

tvals = df.loc[df.blood_test == 't'].hospital.value_counts()
print(f"The answer to the 5th question is {tvals.idxmax()}, {tvals.max()} blood tests")


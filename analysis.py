import pandas as pd
from matplotlib import pyplot as plt
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

df.age.plot(kind='hist', bins=[0, 15, 35, 55, 70, 80])
plt.show()
print("The answer to the 1st question: 15-35")

df.diagnosis.value_counts().plot(kind='pie')
plt.show()
print("The answer to the 2nd question: pregnancy")

fig, axes = plt.subplots()
axes.violinplot(dataset=[df[df.hospital == 'general']["height"].values,
                         df[df.hospital == 'prenatal']["height"].values,
                         df[df.hospital == 'sports']["height"].values] )
plt.show()
print("The answer to the 3rd question: It's because the sports hospital treats mostly athletes and these tend to be taller than the general population.")

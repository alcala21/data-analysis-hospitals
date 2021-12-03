import pandas as pd
pd.set_option('display.max_columns', 8)

dfs = dict()
for name in ["general", "prenatal", "sports"]:
    dfs[name] = pd.read_csv(f"test/{name}.csv")
    dfs[name].drop("Unnamed: 0",axis=1, inplace=True)
    dfs[name].rename(str.lower, axis='columns', inplace=True)
    dfs[name].columns.values[1] = 'gender'

df = pd.concat(dfs, axis=0, ignore_index=True)
print(df.sample(n=20, random_state=30))

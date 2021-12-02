# write your code here
import pandas as pd

pd.set_option('display.max_columns', 8)

names = ["general", "prenatal", "sports"]
dfs = {name: pd.read_csv(f"test/{name}.csv") for name in names}
for name in names:
    print(dfs[name].head(20))

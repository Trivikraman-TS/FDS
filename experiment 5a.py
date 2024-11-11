#experiment no : 5-A

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('d://Trivikraman//FLEX PORT//TECHNICAL//people.csv')
print(df.head(),
df.isnull(),
df.isna(),
df.isna().any(),
df.isna().sum())

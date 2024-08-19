import pandas as pd
# dataframe

# dict
data = {
    'hero': ["Naruto", "Sasuke", "Sakura", "Kakashi"],
    'power level': [9000, 8500, 7000, 9500],
    'Village': ["Leaf", "Leaf", "Leaf", "Leaf"]
}

df_a = pd.DataFrame(data)
print(df_a)

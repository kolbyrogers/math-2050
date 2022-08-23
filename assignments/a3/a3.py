import pandas as pd

x = pd.read_csv("cars.csv")
carData = pd.DataFrame(x)

print("-- Problem 1 --")
print(pd.crosstab(carData.rating, carData.type,
      margins=True, normalize='columns'), '\n')

df = pd.read_csv("heart.csv")

print("-- Problem 2 --")
# i & ii
FBS = pd.crosstab(df.fbs, df.sex, margins=True, normalize='columns')
print("FBS > 120: \n", FBS, '\n')
# iii & iv
midChol = pd.crosstab(df.chol.between(200, 239), df.sex,
                      margins=True, normalize='columns')
print("Serum level 200-239: \n", midChol, '\n')
# v
ht60 = pd.crosstab((df.age > 60), (df.trestbps > 140),
                   margins=True, normalize='columns')
print("Hypertension given age is > 60: \n", ht60)

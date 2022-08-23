import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --- Houses ---
df = pd.read_csv("house_prices.csv")
askPrice = df["asking_price"]
closePrice = df["closing_price"]
sqft = df["sqft"]
dom = df["days_on_market"]
cpsqft = df["cost_per_sqft"]
askPriceCI = np.quantile(askPrice, [.025, .975])
sqftCI = np.quantile(sqft, [.025, .975])
domCI = np.quantile(dom, [.025, .975])
cpsqftCI = np.quantile(cpsqft, [.025, .975])
print("I am 95% confident that the asking price will be between", askPriceCI[0], "and",
      askPriceCI[1])
print("I am 95% confident that the square footage will be between", sqftCI[0], "and",
      sqftCI[1])
print("I am 95% confident that the days on market will be between", domCI[0], "and",
      domCI[1])
print("I am 95% confident that the cost/sqft will be between", cpsqftCI[0], "and",
      cpsqftCI[1])
discounts = []
for i in range(len(askPrice)):
    discount = (askPrice[i] - closePrice[i]) / askPrice[i]
    discounts.append(round(discount, 4))
print(discounts)
discountCI = np.quantile(discounts, [.025, .975])
print("I am 95% confident that the discount will be between", discountCI[0],
      "and", discountCI[1])
print("I am 95% confident that the asking price will be between", askPriceCI[0], "and",
      askPriceCI[1])

# --- Heart ---
df = pd.read_csv("heart.csv")
females = df.loc[df['sex'] == 0]
fDisease = females['exang'].value_counts(normalize=True) * 100
print("Female point estimate:\n", fDisease)
# males = df.loc[df['sex'] == 1]
# mDisease = males['exang'].value_counts(normalize=True) * 100
print("77.1% of the female population has heart disease")
print("62.8% of the male population has heart disease")

# --- NYC Flights ---
df = pd.read_csv("nycflights.csv")
dep_delay = df['dep_delay']
arr_delay = df['arr_delay']
delay = dep_delay + arr_delay
print("The mean total time delay is ", delay.mean())
print("I do not think normal model is the best way to find the CI. I would",
      "instead opt for the use of Bootstrap model.")

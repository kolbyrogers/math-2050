import seaborn as sns
import numpy as np
from scipy import stats
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt


def summary_stats(data):
    stats = {}
    stats["mean"] = np.mean(data)
    stats["median"] = np.median(data)
    stats["std dev"] = np.std(data)
    stats["variance"] = np.var(data)
    stats["range"] = np.max(data) - np.min(data)
    stats["min"] = np.min(data)
    stats["max"] = np.max(data)
    stats["sum"] = np.sum(data)
    stats["count"] = len(data)
    return stats


print("-- Normally Distributed Data --")
data = np.random.normal(0, 15, 200)
data_sorted = np.sort(data)
mean = np.mean(data)
std = np.std(data)
plt.hist(data)
plt.show()
print("Proving using the Three Sigman Rule: ")
print("Probability that a value is within 1 STD: ",
      norm.cdf(std, mean, std) - norm.cdf(-std, mean, std))
print("Probability that a value is within 2 STD: ",
      norm.cdf(2 * std, mean, std) - norm.cdf(-2 * std, mean, std))
print("Probability that a value is within 3 STD: ",
      norm.cdf(3 * std, mean, std) - norm.cdf(-3 * std, mean, std), '\n')


print("-- Sale Price --")
df = pd.read_csv('house-prices-advanced-regression-techniques/train.csv')
price = df["SalePrice"]
stats = (summary_stats(price))
for key in stats:
    print(key, stats[key])
mean = np.mean(price)
std = np.std(price)
sns.histplot(price, kde=True, bins=20)
plt.show()
print("No, the data is not normally distrubuted. Using the Three Sigma Rule: ")
print("Probability that a value is within 1 STD: ",
      norm.cdf(std, mean, std) - norm.cdf(-std, mean, std))
print("Probability that a value is within 2 STD: ",
      norm.cdf(2 * std, mean, std) - norm.cdf(-2 * std, mean, std))
print("Probability that a value is within 3 STD: ",
      norm.cdf(3 * std, mean, std) - norm.cdf(-3 * std, mean, std))
# remove missing values
df.dropna(subset=['SalePrice'])
print("-- Missing values removed--")
# remove outliers
q_low = df["SalePrice"].quantile(0.01)  # q1 + (1.5 * IQR)
q_hi = df["SalePrice"].quantile(0.99)  # q3 + (1.5* IQR)
df = df[(df["SalePrice"] < q_hi) & (df["SalePrice"] > q_low)]
print("-- Outliers removed --\n")
price = df['SalePrice']
standardPrice = (price - price.mean()) / price.std()
sns.histplot(standardPrice, kde=True, bins=20)
plt.show()
print("-- Data Standardized --\n")
logPrice = np.log2(price)
sns.histplot(logPrice, kde=True, bins=20)
plt.show()
print("-- Logarithmic Transformation --\n")
print("Taking the logarithmic transformation of the data seems to have made the data even closer to being normally distributed")


print("-- Great Room Living Area --")
df = pd.read_csv('house-prices-advanced-regression-techniques/train.csv')
price = df["GrLivArea"]
stats = (summary_stats(price))
for key in stats:
    print(key, stats[key])
mean = np.mean(price)
std = np.std(price)
sns.histplot(price, kde=True, bins=20)
plt.show()
print("No, the data is not normally distrubuted. Using the Three Sigma Rule: ")
print("Probability that a value is within 1 STD: ",
      norm.cdf(std, mean, std) - norm.cdf(-std, mean, std))
print("Probability that a value is within 2 STD: ",
      norm.cdf(2 * std, mean, std) - norm.cdf(-2 * std, mean, std))
print("Probability that a value is within 3 STD: ",
      norm.cdf(3 * std, mean, std) - norm.cdf(-3 * std, mean, std))
# remove missing values
df.dropna(subset=['GrLivArea'])
print("-- Missing values removed--")
# remove outliers
q_low = df["GrLivArea"].quantile(0.01)
q_hi = df["GrLivArea"].quantile(0.99)
df = df[(df["GrLivArea"] < q_hi) & (df["GrLivArea"] > q_low)]
print("-- Outliers removed --\n")
price = df["GrLivArea"]
standardPrice = (price - price.mean()) / price.std()
sns.histplot(standardPrice, kde=True, bins=20)
plt.show()
print("-- Data Standardized --\n")
print("The great room living area data is more normally distributed AFTER removing outliers")


print("-- Total Basement Square Footage --")
df = pd.read_csv('house-prices-advanced-regression-techniques/train.csv')
price = df["TotalBsmtSF"]
stats = (summary_stats(price))
for key in stats:
    print(key, stats[key])
mean = np.mean(price)
std = np.std(price)
sns.histplot(price, kde=True, bins=20)
plt.show()
print("No, this data is very close to being normally distrubuted, but is not. Using the Three Sigma Rule: ")
print("Probability that a value is within 1 STD: ",
      norm.cdf(std, mean, std) - norm.cdf(-std, mean, std))
print("Probability that a value is within 2 STD: ",
      norm.cdf(2 * std, mean, std) - norm.cdf(-2 * std, mean, std))
print("Probability that a value is within 3 STD: ",
      norm.cdf(3 * std, mean, std) - norm.cdf(-3 * std, mean, std))
# remove missing values
df.dropna(subset=['TotalBsmtSF'])
print("-- Missing values removed--")
# remove outliers
q_low = df["TotalBsmtSF"].quantile(0.01)
q_hi = df["TotalBsmtSF"].quantile(0.99)
df = df[(df["TotalBsmtSF"] < q_hi) & (df["TotalBsmtSF"] > q_low)]
print("-- Outliers removed --")
price = df["TotalBsmtSF"]
standardPrice = (price - price.mean()) / price.std()
sns.histplot(standardPrice, kde=True, bins=20)
plt.show()
print("-- Data Standardized --\n")
print("Using the basement square footage produced more normally distributed data than either of the others")

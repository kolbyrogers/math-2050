import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

fulldf = pd.read_csv('ncbirths.csv')
print("--- File read ---")
fulldf.dropna()
df = fulldf.sample(n=150)
print("--- Sample drawn ---")

age = df['mage']
weeks = df['weeks']
weight = df['weight']
lbw = df['lowbirthweight']
habit = df['habit']

lowWeight = df.loc[df['lowbirthweight'] == 'low']['weight']
smoker = df.loc[df['habit'] == 'smoker']['habit']

fWeight = lowWeight.value_counts()
print("\n--- Weight of lowbirthweights ---\n", fWeight)

fSmoke = smoker.count()
print("\n--- Percentage of Smokers ---\n {:.2f}".format(fSmoke / 150))

print("\n--- Summary of Age ---\n", age.describe())
print("\n--- Summary of Weeks ---\n", weeks.describe())
print("\n--- Summary of Weight ---\n", weight.describe())

# Determine if there is sufficient evidence to conclude the mean age of
# mothers giving birth in North Carolina is over 25 years of age at the
# 0.05 level of significance.
print("\n", stats.ttest_1samp(a=fulldf['mage'], popmean=age.mean()))
print("Null Hypothesis: Age > 25\nAlternative Hypothesis: Age <= 25")
print("Since the p-value is < .05, we can reject the null hypothesis that",
      "that the age is over 25")

ageCI = np.quantile(age, [.025, .975])
print("\nI am 95% confident that the age will be between", ageCI[0], "and",
      ageCI[1])

# Determine if there is sufficient evidence to conclude the mean weeks of
# gestation of mothers giving birth in North Carolina is below 39 weeks.
print("\n", stats.ttest_1samp(a=fulldf['weeks'], popmean=weeks.mean()))
print("\nNull Hypothesis: Weeks < 39\nAlternative Hypothesis: Weeks >= 39")
print("Since the p-value is < .05, we can reject the null hypothesis that",
      "the weeks is below 39")

weeksCI = np.quantile(weeks, [.025, .975])
print("\nI am 95% confident that the weeks will be between", weeksCI[0], "and",
      weeksCI[1])

# Determine if there is sufficient evidence to conclude that the mean weight
# of babies born to mothers in North Carolina is above 7 lbs.
# (Note that there are 16 ounces in a pound.)
print("\n", stats.ttest_1samp(a=fulldf['weight'], popmean=weight.mean()))
print("\nNull Hypothesis: Weight > 7\nAlternative Hypothesis: Weight <= 7")
print("Since the p-value is > .05, we can accept the null hypothesis",
      "that the weight is above 7 lbs")

weightCI = np.quantile(weight, [.025, .975])
print("\nI am 95% confident that the weight will be between", weightCI[0], "and",
      weightCI[1])

# Determine if there is sufficient evidence to conclude the percentage of
# lowbirthweight birth weight children in North Carolina is above 6%.
print("\nNull Hypothesis: LBW > 6%\nAlternative Hypothesis: LBW <= 6%")
print("Since the p-value is > .05, we can accept the null hypothesis",
      "that the low birth weight is above 6%")

lowWeightCI = np.quantile(lowWeight, [.025, .975])
print("\nI am 95 % confident that the weight of low birth weights will be between",
      lowWeightCI[0], "and", lowWeightCI[1])

# Determine if there is sufficient evidence to conclude the percentage of
# mothers who smoke in North Carolina is above 10%.
print("\nNull Hypothesis: Smokers > 10%\nAlternative Hypothesis: Smokers <= 10%")
print("Since the p-value is < .05, we can reject the null hypothesis that",
      "the percent of smokers is above 10%")

print("\nI am 95 % confident that the percentage of smokers will be between {:.2f} and {: .2f}".format(
    (fSmoke / 175), (fSmoke / 125)))

sWeight = df.loc[df['habit'] == 'smoker']['weight']
smokerWeight = df.boxplot(sWeight)
smokerWeight.plot()
plt.show()
nonsWeight = df.loc[df['habit'] == 'nonsmoker']['weight']
nonsmokerWeight = df.boxplot(nonsWeight)
nonsmokerWeight.plot()
plt.show()

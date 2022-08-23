from bioinfokit.analys import stat
from statsmodels.formula.api import ols
import statsmodels.api as sm
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

print("--Q1--")
df = pd.read_csv("guardian.csv")
print("Null Hypothesis: Guardian impacts final grade")
print("Alternate Hypothesis: Guardian does NOT impact final grade\n")

# reshape the d dataframe suitable for statsmodels package
df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['father',
                                                                   'mother', 'other'])
# replace column names
df_melt.columns = ['index', 'guardian', 'value']

# generate a boxplot to see the data distribution by treatments. Using boxplot, we can
# easily detect the differences between different treatments
ax = sns.boxplot(x='guardian', y='value', data=df_melt, color='#99c2a2')
ax = sns.swarmplot(x="guardian", y="value", data=df_melt, color='#7d0013')
plt.show()

# stats f_oneway functions takes the groups as input and returns ANOVA F and p value
fvalue, pvalue = stats.f_oneway(df['father'], df['mother'], df['other'])
print("\nF-value:", fvalue, "P-value:", pvalue, "\n")

# Ordinary Least Squares (OLS) model
model = ols('value ~ C(guardian)', data=df_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# ANOVA table using bioinfokit v1.0.3 or later (it uses wrapper script for anova_lm)
res = stat()
res.anova_stat(df=df_melt, res_var='value',
               anova_model='value ~ C(guardian)')
print(res.anova_summary)

# note: if the data is balanced (equal sample size for each group), Type 1, 2, and 3 sums of squares
# (typ parameter) will produce similar results.

# perform multiple pairwise comparison (Tukey's HSD)
# unequal sample size data, tukey_hsd uses Tukey-Kramer test
# res = stat()
# res.tukey_hsd(df=df_melt, res_var='value', xfac_var='guardian',
# anova_model='value ~ C(guardian)')
# print(res.tukey_summary)

print("\nSince the p-value is < 0.05, we can conclude that there is an impact by\
 the guardian on the final grade")

print("\n--Q2--")
df = pd.read_csv("bipolar_disorder.csv")

print("Null Hypothesis: Group means are equal")
print("Alternate Hypothesis: Group means are NOT equal")

# reshape the d dataframe suitable for statsmodels package
df_melt = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['Bipolar',
                                                                   'Control',
                                                                   'Ud'])
# replace column names
df_melt.columns = ['index', 'right_answers', 'value']

# generate a boxplot to see the data distribution by treatments. Using boxplot, we can
# easily detect the differences between different treatments
ax = sns.boxplot(x='right_answers', y='value', data=df_melt, color='#99c2a2')
ax = sns.swarmplot(x="right_answers", y="value", data=df_melt, color='#7d0013')
plt.show()

# stats f_oneway functions takes the groups as input and returns ANOVA F and p value
fvalue, pvalue = stats.f_oneway(df['Bipolar'], df['Control'], df['Ud'])
print("\nF-value:", fvalue, "P-value:", pvalue, "\n")

# Ordinary Least Squares (OLS) model
model = ols('value ~ C(right_answers)', data=df_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# ANOVA table using bioinfokit v1.0.3 or later (it uses wrapper script for anova_lm)
res = stat()
res.anova_stat(df=df_melt, res_var='value',
               anova_model='value ~ C(right_answers)')
print(res.anova_summary)

# note: if the data is balanced (equal sample size for each group), Type 1, 2, and 3 sums of squares
# (typ parameter) will produce similar results.

# perform multiple pairwise comparison (Tukey's HSD)
# unequal sample size data, tukey_hsd uses Tukey-Kramer test
res = stat()
res.tukey_hsd(df=df_melt, res_var='value', xfac_var='right_answers',
              anova_model='value ~ C(right_answers)')
print(res.tukey_summary)

print("\nSince the p-value is < 0.05, we can conclude that there is an impact by\
 the group on the right answers")

print("\n--Q3--")
white_alone = pd.read_csv("white_alone.csv")
print("Null Hypothesis: Gender has an impact on mean income")
print("Alternate Hypothesis: Gender does NOT have an impact on mean impact")
# reshape the d dataframe suitable for statsmodels package
df_melt = pd.melt(white_alone.reset_index(), id_vars=['index'], value_vars=['Male',
                                                                            'Female'])
# replace column names
df_melt.columns = ['index', 'gender', 'value']

# generate a boxplot to see the data distribution by treatments. Using boxplot, we can
# easily detect the differences between different treatments
ax = sns.boxplot(x='gender', y='value', data=df_melt, color='#99c2a2')
ax = sns.swarmplot(x="gender", y="value", data=df_melt, color='#7d0013')
plt.show()

# stats f_oneway functions takes the groups as input and returns ANOVA F and p value
fvalue, pvalue = stats.f_oneway(white_alone['Male'], white_alone['Female'])
print("\nF-value:", fvalue, "P-value:", pvalue, "\n")

# Ordinary Least Squares (OLS) model
model = ols('value ~ C(gender)', data=df_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# ANOVA table using bioinfokit v1.0.3 or later (it uses wrapper script for anova_lm)
res = stat()
res.anova_stat(df=df_melt, res_var='value',
               anova_model='value ~ C(gender)')
print(res.anova_summary)

# note: if the data is balanced (equal sample size for each group), Type 1, 2, and 3 sums of squares
# (typ parameter) will produce similar results.

print("\nSince the p-value is much < 0.05, we can conclude that there is an impact by\
 the gender on the mean income")
white_black = pd.read_csv("white_black.csv")
print("Null Hypothesis: Race has an impact on mean income")
print("Alternate Hypothesis: Race does NOT have an impact on mean impact")
# reshape the d dataframe suitable for statsmodels package
df_melt = pd.melt(white_black.reset_index(), id_vars=['index'],
                  value_vars=['black-male',
                              'black-female', 'white-male', 'white-female'])
# replace column names
df_melt.columns = ['index', 'gender', 'value']

# generate a boxplot to see the data distribution by treatments. Using boxplot, we can
# easily detect the differences between different treatments
ax = sns.boxplot(x='gender', y='value', data=df_melt, color='#99c2a2')
ax = sns.swarmplot(x="gender", y="value", data=df_melt, color='#7d0013')
plt.show()

# stats f_oneway functions takes the groups as input and returns ANOVA F and p value
fvalue, pvalue = stats.f_oneway(white_black['black-male'],
                                white_black['black-female'], white_black['white-male'],
                                white_black['white-female'])
print("\nF-value:", fvalue, "P-value:", pvalue, "\n")

# Ordinary Least Squares (OLS) model
model = ols('value ~ C(gender)', data=df_melt).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

# ANOVA table using bioinfokit v1.0.3 or later (it uses wrapper script for anova_lm)
res = stat()
res.anova_stat(df=df_melt, res_var='value',
               anova_model='value ~ C(gender)')
print(res.anova_summary)
print("\nSince the p-value is much < 0.05, we can conclude that there is an impact by\
 the race on the mean income")

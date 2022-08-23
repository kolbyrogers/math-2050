import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('Solarize_Light2')


def checkNormal(data, name):
    # Checks if given variable is normally distributed
    k2, p = stats.normaltest(data)
    alpha = 0.05
    print("P = {:g}".format(p))
    if p < alpha:
        print("Since P is < 0.05, we can reject the null hypothesis and\
 conclude that {:s} is normally distributed".format(name))
    else:
        print("Since P is >= 0.05, the null hypothesis cannot be rejected and\
 we can conclude {:s} is NOT normally distributed".format(name))


df = pd.read_csv('coasters.csv')
print("This data contains information about over 1000 rollercoasters.")
print("Information was scraped from wikipedia.")
print("This data consists of many characteristic such as speed, length,\
 construction material, opening date, etc.\n")

# Shows a histogram of the speed of each coaster.
ax = df["speed_mph"].plot(
    kind="hist",
    figsize=(12, 8),
    bins=60,
    title="Coaster Speeds"
)
ax.set_xlabel("Speed (mph)")
plt.show()

# Shows a scatter plot of year introduced vs speed.
ax = df.plot(
    x="year_introduced",
    y="speed_mph",
    figsize=(12, 8),
    style=".",
    color="black",
)
ax.set_title("Coaster Year vs Speed", fontsize=20)
ax.set_xlabel("Year Introduced")
ax.set_ylabel("Speed (mph)")
ax.legend().remove()
plt.show()

# Shows a scatter plot of height vs speed using year introduced.
fig, ax = plt.subplots(figsize=(10, 10))

sns.scatterplot(
    x="height_ft",
    y="speed_mph",
    data=df,
    hue="year_introduced",
)
plt.show()

# Shows a histogram of the GForce of each coaster
ax = df["Gforce_clean"].plot(
    kind="hist",
    bins=50,
    figsize=(12, 8),
)
ax.set_title("Coaster GForce", fontsize=20)
ax.set_xlabel("G-Force")
plt.show()

# Prints the numerical summarization of the entire dataset.
print("Numerical Summarization of data:\n", df.describe())


# Uses stats.normaltest to determine whether variables are normally distributed.
print("\nChecking if speed is normally distributed:")
checkNormal(df["speed_mph"].dropna(), "Speed")

print("\nChecking if height is normally distributed:")
checkNormal(df["height_ft"].dropna(), "Height")

print("\nChecking if inversion count is normally distributed:")
checkNormal(df["Inversions_clean"].dropna(), "Inversion count")

print("\nChecking if GForce is normally distributed:")
checkNormal(df["Gforce_clean"].dropna(), "GForce")

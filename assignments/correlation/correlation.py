import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sci

print('--- Q1 ---')

x = np.array([5, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12])
y = np.array([4.2, 5, 5.2, 5.9, 6, 6.2, 6.1, 6.9,
             7.2, 8, 8.3, 7.4, 8.4, 7.8, 8.5, 9.5])
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlim(0, 30)
plt.ylim(0, 20)
plt.show()

LCC = sci.pearsonr(x, y)
print("Linear correlation coefficient:", LCC)

x = x * 2
y = y * 2
print("--- X and Y multiplied by 2 ---")

plt.scatter(x, y)
plt.title('Scatter Plot 2x and 2y')
plt.xlim(0, 30)
plt.ylim(0, 20)
plt.show()

LCC = sci.pearsonr(x, y)
print("New linear correlation coefficient:", LCC)
print("The correlation coeficcient does not change because the *RELATION* of all the numbers stayed the same.\n")

print("--- Q2 ---")

cases = np.array([3, 2, 2, 4, 5, 15, 22, 13, 6, 5, 4, 1])
deaths = np.array([0, 1, 2, 1, 2, 9, 16, 5, 3, 3, 1, 0])
plt.scatter(cases, deaths)
plt.title('Scatter Plot')
plt.xlabel("Cases of lyme disease")
plt.ylabel("Drowning deaths")
plt.show()
print("It appears that cases of lyme disease and drowning deaths have a positve, linear relation.")
print("I do not believe that increasing lyme disease will increase drowning deaths.")
print("The lurking variable is the month in which the data was recorded.\n")

print("--- Q3 ---")

df = pd.read_csv('mri.csv')
mri = df['mri']
iq = df['iq']
gender = df['gender']
plt.scatter(mri, iq)
plt.title('Scatter Plot')
plt.xlabel("MRI count")
plt.ylabel("IQ")
plt.show()

LCC = sci.pearsonr(mri, iq)
print("Linear correlation coefficient:", LCC)
print("MRI count and IQ are somewhat linearly related")

plt.scatter(mri, iq, c=gender)
plt.title('Scatter Plot by Gender')
plt.xlabel("MRI count")
plt.ylabel("IQ")
plt.show()
print("Males seem to have higher MRI count and IQ")

femaleMRI = df.loc[(df['gender'] == 0, 'mri')]
femaleIQ = df.loc[(df['gender'] == 0, 'iq')]
LCC = sci.pearsonr(femaleMRI, femaleIQ)
print("Linear correlation coefficient for Females:", LCC)

maleMRI = df.loc[(df['gender'] == 1, 'mri')]
maleIQ = df.loc[(df['gender'] == 1, 'iq')]
LCC = sci.pearsonr(maleMRI, maleIQ)
print("Linear correlation coefficient for Males:", LCC)

print("\n--- Q4 ---")

df = pd.read_csv('traffic.csv')
male = df['males']
female = df['females']
mcrash = df['mcrash']
fcrash = df['fcrash']

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.scatter(male, mcrash, s=10, c='b', marker="s", label='male')
ax1.scatter(female, fcrash, s=10, c='r', marker="o", label='female')
plt.legend(loc='upper left')
plt.title('Scatter Plot')
plt.xlabel("licensed drivers")
plt.ylabel('fatal crashes')
plt.show()
print("Yes. It seems that males are more often involved in fatal crashes.")
LCC = sci.pearsonr(male, mcrash)
print("Linear correlation coefficient for Males:", LCC)
LCC = sci.pearsonr(female, fcrash)
print("Linear correlation coefficient for Females:", LCC)
print("Males have a slightly higher linear relation between licensed drivers and fatal crashes.")

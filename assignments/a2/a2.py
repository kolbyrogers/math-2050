import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Question 1
print("---Question 1---")
df = pd.read_csv('3_r_3.csv')
age = df["Age"]
print("A: Mean age:", age.mean(), "- Median age:", age.median(), "- Mode age(s):", age.mode().values) 
# TODO- print("Range: ", age.range(),'\n')
print("B: Range:", np.ptp(np.array(age)),"- Standard Deviation:", age.std())
sample1 = age.sample(4)
sample2 = age.sample(4)

print("C: Sample means: ", sample1.mean(), "&", sample2.mean(), "Sample Standard Deviations:", sample1.std(), "&", sample2.std())

# Question 2
print("\n---Question 2---")
df = pd.read_csv('3_r_4.csv')
tickets = df["Tickets Issued"]
plt.hist(tickets)
plt.title("Tickets Issued")
plt.show()
print("B: Mean would be higher than the Median")
print("C: Mean:", tickets.mean(), "- Median:", tickets.median())
print("D: Mode: ", tickets.mode().values)

# Question 3
print("\n---Question 3---")
df = pd.read_csv('3_r_10.csv')
pia = df["Presidential Inaugural Addresses"]
print("A: Mean:", pia.mean(), "- Median:", pia.median())
print("B: Q1:", pia.quantile([0.25]).values, "- Q3:", pia.quantile([0.75]).values)
print("C: Min:", np.min(pia), "- Max:", np.max(pia), "- STD:", np.std(pia), "- Mean:",np.mean(pia), "- Median:",np.median(pia))
print("D: STD:", np.std(pia), "- IQR:", np.subtract(*np.percentile(pia, [75, 25])))
print("E: Yes")
plt.boxplot(pia)
plt.title("Words in Presidential Inaugural Addresses")
plt.show()
print("G: The data is very slightly skewed right. The Q3 is further from the median than the Q1 is and there are more outliers on the higher end")
print("H: Because there are several outliers, the Median is the best measure of central tendency")
print("I: I think that the IQR is the best measure of dispersion")
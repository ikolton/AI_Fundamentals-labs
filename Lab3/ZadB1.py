import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Wygeneruj dane 10. wymiarowe tak by
# 1 3 5 współrzedna były skorelowane ze sobą dodatnio
# 7 8 współrzedna były skorelowane ze sobą ujemnie
# pozostałe były nieskorelowane

n = 1000
x1 = stats.norm(0, 1).rvs(n)
x2 = stats.norm(0, 1).rvs(n)
x3 = 2*x1
x4 = x1 + stats.norm(0, 1).rvs(n)
x5 = 3*x1
x6 = x1 + stats.norm(0, 1).rvs(n)
x7 = stats.norm(0, 1).rvs(n)
x8 = -x7
x9 = stats.norm(0, 1).rvs(n)
x10 = stats.norm(0, 1).rvs(n)

X=np.stack((x1,x2,x3,x4,x5,x6,x7,x8,x9,x10),axis=1)

df=pd.DataFrame(X)
sns.pairplot(df)
#plt.show()

#Proszę zwizualizować tą zależność za pomocą

# - sns.pairplot
# - sns.heatmap

sns.set(style="darkgrid")

corr = df.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool_)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmin=-1, vmax=1,
            square=True, xticklabels=5, yticklabels=5,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
plt.show()
print(corr)
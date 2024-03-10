import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

#inFile = 'http://ww2.amstat.org/publications/jse/datasets/babyboom.dat.txt'
data = pd.read_csv("babyboom.dat.txt", sep='[ ]+', header=None, engine='python',names= ['sex', 'Weight', 'Minutes'])

df = data[['Minutes', 'sex', 'Weight']]

grouped = df.groupby('sex')

# Wykres w kształcie szeregu czasowego dla każdej grupy
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['blue', 'red']  # Definicja różnych kolorów dla każdej grupy
for i, (name, group) in enumerate(grouped):
    ax.plot(group['Minutes'], group['Weight'], marker='o', linestyle='', ms=5, label=name, color=colors[i])
ax.set_xlabel('Minutes')
ax.set_ylabel('Weight')
ax.set_title('Wykres w kształcie szeregu czasowego')
ax.legend()
plt.show()


# Histogramy dla każdej grupy
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
for i, (name, group) in enumerate(grouped):
    axs[i].hist(group['Weight'], bins=10, alpha=0.5, label=name)
    axs[i].set_title('Histogram dla grupy {}'.format(name))
    axs[i].set_xlabel('Weight')
    axs[i].set_ylabel('Frequency')
    axs[i].legend()
plt.show()

# Estymacje gęstości dla każdej grupy
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
for i, (name, group) in enumerate(grouped):
    group['Weight'].plot.kde(ax=axs[i])
    axs[i].set_title('Estymacja gęstości dla grupy {}'.format(name))
    axs[i].set_xlabel('Weight')
    axs[i].set_ylabel('Density')
plt.show()

#alternatywna estymacja gęstości z użyciem sns
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
for i, (name, group) in enumerate(grouped):
    sns.kdeplot(group['Weight'], ax=axs[i])
    axs[i].set_title('Estymacja gęstości dla grupy {}'.format(name))
    axs[i].set_xlabel('Weight')
    axs[i].set_ylabel('Density')
plt.show()

# Dystrybuanty empiryczne dla każdej grupy
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
for i, (name, group) in enumerate(grouped):
    group['Weight'].plot.hist(cumulative=True, density=1, bins=50, ax=axs[i])
    axs[i].set_title('Dystrybuanta empiryczna dla grupy {}'.format(name))
    axs[i].set_xlabel('Weight')
    axs[i].set_ylabel('Cumulative Probability')
plt.show()

#alternatywne dystrybuanty empiryczne z użyciem scipy - stats
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
for i, (name, group) in enumerate(grouped):
    cumulative_freq = stats.cumfreq(group['Weight'], numbins=50)
    axs[i].plot(cumulative_freq[0], label=name)
    axs[i].set_title('Dystrybuanta empiryczna dla grupy {}'.format(name))
    axs[i].set_xlabel('Weight')
    axs[i].set_ylabel('Cumulative Frequency')
    axs[i].legend()
plt.show()

# Wykresy pudełkowe dla każdej grupy
fig, ax = plt.subplots(figsize=(8, 6))
df.boxplot(column='Weight', by='sex', ax=ax)
ax.set_title('Wykresy pudełkowe dla każdej grupy')
ax.set_ylabel('Weight')
plt.show()

# Alternatywne wykresy pudełkowe z użyciem plt.boxplot
fig, ax = plt.subplots(figsize=(8, 6))
data_grouped = [group['Weight'].values for name, group in grouped]
plt.boxplot(data_grouped, sym='*')
ax.set_title('Alternatywne wykresy pudełkowe dla każdej grupy')
ax.set_ylabel('Weight')
ax.set_xticklabels([name for name, group in grouped])
plt.show()


# Wykresy skrzypcowe dla każdej grupy
fig, ax = plt.subplots(figsize=(8, 6))
sns.violinplot(x='sex', y='Weight', data=df, ax=ax)
ax.set_title('Wykresy skrzypcowe dla każdej grupy')
ax.set_ylabel('Weight')
plt.show()



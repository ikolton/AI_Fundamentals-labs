import numpy as np
import pandas as pd

#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
#1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S

df = pd.read_csv('https://github.com/Ulvi-Movs/titanic/raw/main/train.csv')
print(df.shape)
# df.head()
print(df.columns)

#zad6
#Usuń kolumny: "PassengerId", "Name" i "Ticket".

# Powody:
#
#   * PassengerId - jest to unikalny numer
#   * Imię - nie ma wpływu na predykcje
#   * Bilet - wygląda niechlujnie i jest losowe

df = df.drop(columns=["PassengerId", "Name", "Ticket"])
print(df.shape)
print(df.columns)

# # Zadanie 7
# Utwórz nową kolumną o nazwie HasCabin, która zawiera 1 jeżeli ktoś miał swoją kabinę i 0 jeśli nie.

df['HasCabin'] = df['Cabin'].notna().astype(int)
print(df['HasCabin'])

# Zadanie 8
# Usuń brakujące wartości
print("Brakujące wartości")
print(df.shape)
# print(df.isna().sum())
df = df.dropna()
# print(df.isna().sum())
print(df.shape)

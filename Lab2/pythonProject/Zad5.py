import numpy as np
import pandas as pd

# Zaimportuj dane z pliku ,,airports.csv'' i wykonaj na nich poniższe polecenia:
#
#   * wybierz nazwy państw ostatnich 12 lotnisk w tabeli,
#   * wybierz wiersz o indeksie 1 korzystając z indeksera .loc oraz .iloc (porównaj otrzymane wyniki),
#   * wybierz wszystkie lotniska w Polsce,
#   * wybierz wszystkie lotniska, których nazwa różni się od nazwy miasta, w którym się znajdują.
#   * przelicz wartości wysokości na metry i zapisz zmodyfikowaną kolumnę w miejsce starej (w naszej tabeli wysokość jest podana w   * stopach nad poziomem morza; jedna stopa angielska równa się 30,48 cm),
#   * znajdź wszystkie państwa, w których znajduje się wyłącznie 1 lotnisko (zobacz procedurę .unique()).
#przykładowe dane 323361,"00AA","small_airport","Aero B Ranch Airport",38.704022,-101.473911,3435,"NA","US","US-KS","Leoti","no","00AA",,"00AA",,,
# 6524,"00AK","small_airport","Lowell Field",59.947733,-151.692524,450,"NA","US","US-AK","Anchor Point","no","00AK",,"00AK",,,

data = pd.read_csv("airports.csv", header=None)

print("iloc[-12:, 3]")
print(data.iloc[-12:, 3])
print("\nloc")
print(data.loc[1])
print("\niloc")
print(data.iloc[1])
print("\nPL airports:")
print(data.loc[data[8] == "PL", [3, 8, 17]])
print("\nMiasto != nazwa lotniska:")
print(data.loc[data[3] != data[10], [3, 10]])
print("\n")
metersData = data.copy()
metersData[6] = pd.to_numeric(metersData[6], errors='coerce')
metersData[6] = metersData[6] * 0.3048
print(metersData[6])
#   * znajdź wszystkie państwa, w których znajduje się wyłącznie 1 lotnisko (zobacz procedurę .unique()).
print("\n")
print(data.loc[data[8].isin(data[8].value_counts()[data[8].value_counts() == 1].index), 8].unique())

print(data[8].value_counts()[data[8].value_counts() == 1])




#
# Obligatorisk arbeidskrav / innlevering 1, PY1010 USN
# Koden sammenligner kostnader for 1 år med elbil vs bensinbil
#

# default kjørelengde i km
kjorelengde = 10000

# årspris for forsikring
forsikring_elbil = 5000
forsikring_bensinbil = 7500

# trafikkforsikringsavgift for 1 år
aarsavgift = 8.38*365 # dagspris * 365 for å finne årspris

# forbruk i kroner per km
forbruk_elbil = 0.2*2 # forbruk: 0,2 kWh/km - strømpris: 2.00 kr/kWh
forbruk_bensinbil = 1 # 1 kr / km

# bomavgifter i kroner per km
bomavgift_elbil = 0.10
bomavgift_bensinbil = 0.30

# beregning og utskrift av årlig kostnad elbil
kostnad_el = forsikring_elbil + aarsavgift + (kjorelengde*forbruk_elbil) + (kjorelengde*bomavgift_elbil)
print("\nÅrlig kostnad for elbil med kjørelengde", kjorelengde, "km :", format(kostnad_el, '.2f'), "kr")

# beregning og utskrift av årlig kostnad bensinbil
kostnad_bensin = forsikring_bensinbil + aarsavgift + (kjorelengde*forbruk_bensinbil) + (kjorelengde*bomavgift_bensinbil)
print("Årlig kostnad for bensinbil med kjørelengde", kjorelengde, "km :", format(kostnad_bensin, '.2f'), "kr")

# beregning og utskrift av årlig kostnadsdifferanse
diff = kostnad_el - kostnad_bensin
print("\nÅrlig kostnadsdifferanse for elbil vs bensinbil :", format(diff, '.2f'), "kr")
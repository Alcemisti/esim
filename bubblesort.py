# Lista, joka sisältää 5 eri numeroa
numerot = [23, 234, 12, 5, 3, 6543]

# Kuplalajittelu (bubble sort) for-silmukalla
for i in range(len(numerot)):
    # Käydään lista läpi, ja jokaisella kierroksella suurin alkio kuplii loppuun
    for j in range(0, len(numerot) -i - 1):
        # Vaihdetaan vierekkäiset, jos ne ovat väärässä järjestyksessä
        if numerot[j] > numerot[j + 1]:
            # Vaihto tapahtuu tässä
            numerot[j], numerot[j + 1] = numerot[j +1], numerot[j]

# Tulostetaan järjestetty lista
print(numerot)
# 14. feladat – Kocka
# A program olvasson be a konzolról egy egész számot! Ha a szám pozitív, akkor legyen a beolvasott szám egy kocka élének hossza. A program számítsa ki és írja ki a kocka felszínét, térfogatát a konzolra! Ha a szám nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kocka élének hossza nem pozitív!"!

szam1 = int(input("Adjon meg egy egész számot!"))

if szam1 > 0:
    print("A kocka felszíne: ", str(6*(szam1**2)))
    print("A kocka térfogata: ", str(szam1**3))
else:
    print("Hiba: a kocka élének hossza nem pozitív!")
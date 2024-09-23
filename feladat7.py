# 7. feladat – Négyzetgyök
# A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!

import math

szam1 = float(input("Adj meg egy valós számot!"))

if szam1 >= 0:
    print("A szám négyzetgyöke:", str(math.sqrt(szam1)))
else:
    print("Hiba: negatív számból nem lehet négyzetgyököt vonni!")
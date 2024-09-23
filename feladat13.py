# 13. feladat – Kör
# A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!

import math

korSugar = float(input("Adja meg a kör sugarát!"))

if korSugar > 0:
    print("A kör kerülete: ", str(korSugar*2*math.pi))
    print("A kör területe: ", str(korSugar**2*math.pi))
else:
    print("Hiba: a kör sugara nem pozitív!")
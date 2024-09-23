# 15. feladat – Téglalap1
# A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"

a = float(input("Adja meg a téglalap egyik oldalát!"))
b = float(input("Adja meg a téglalap másik oldalát!"))

if (a > 0) and (b > 0):
    print("A téglalap kerülete: ", str(round(2*(a+b), 2)))
    print("A téglalap területe: ", str(round(a*b, 2)))
else:
    print("Hiba: a téglalap oldalai nem pozitívak!")
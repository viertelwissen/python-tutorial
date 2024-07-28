geheime_zahl = 56
eingabe = -1
versuche = 0

while eingabe != geheime_zahl:
    eingabe = input("Rate die gesuchte Zahl: ")

    if eingabe == "exit":
        break

    if eingabe.isdecimal():
        eingabe = int(eingabe)
    else:
        print("Ungültige Eingabe!")
        break

    if eingabe < geheime_zahl:
        print("Die gesuchte Zahl ist größer.")
    elif eingabe > geheime_zahl:
        print("Die gesuchte Zahl is kleiner.")
    versuche += 1
else:
    print("Zahl in {} Versuchen erraten.".format(versuche))

print("Programm beendet.")

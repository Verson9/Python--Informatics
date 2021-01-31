nr, tp, po, fp, fk=input("" ).split(" ")
fph = fp[0]+fp[1]
fpm = fp[3]+fp[4]
fkh = fk[0]+fk[1]
fkm = fk[3]+fk[4]


litery = {
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "R",
    "S",
    "T",
    "U",
    "W",
    "Y",
    "Z",
    "X",
    "Q",
    "V"
}
liczby = {
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0"
}
liczbya = {
    "0",
    "1",
    "2"
}
liczbyb = {
    "0",
    "1",
    "2",
    "3",
    "4",
    "5"
}

if fp[0] in list(liczbya) and fp[1] in list(liczby) and fp[2] == ":" and fp[3] in list(liczbyb) and fp[4] in list(liczby) and fk[0] in list(liczbya) and fk[1] in list(liczby) and fk[2] == ":" and fk[3] in list(liczbyb) and fk[4] in list(liczby) and int(fph)<24 and int(fpm)<60 and int(fkh)<24 and int(fkm)<60 and nr[0] in list(litery) and nr[1] in list(litery) and nr[2] in list(liczby) and nr[3] in list(liczby) and nr[4] in list(liczby) and nr[5] in list(liczby) and tp == "S" or tp == "C":
    s=int(po)
    hfp = int(fph)
    mfp = int(fpm)
    hfk = int(fkh)
    mfk = int(fkm)
    if hfp>hfk:
        hfk=hfk+24
    if mfp>mfk:
        hfk=hfk-1
        mfk=mfk+60
    minuty_fp = hfp * 60 + mfp
    minuty_fk = hfk * 60 + mfk
    godziny_fp = minuty_fp / 60
    godziny_fk = minuty_fk / 60
    v=s/1000/(godziny_fk-godziny_fp)


    if round(v, 2)>80 and tp == "C":
        mandat="M"
    elif round(v, 2)>140 and tp == "S":
        mandat="M"
    else:
        mandat="."

    print(nr," ", mandat," ", round(v, 2))
else:
    print("BLAD")




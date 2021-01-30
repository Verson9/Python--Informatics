nr = input('Podaj numer rejestracyny pojazdu')
tp = input('Podaj typ pojazdu')
po = input('Podaj przejechaną odległość w metrach')
fp = input('Podaj godzinę przejazdu przez pierwszy fotoradar')
fk = input('Podaj godzinę przejazdu przez drugi fotoradar')
fph = fp[0]+fp[1]
fpm = fp[3]+fp[4]
fkh = fk[0]+fk[1]
fkm = fk[3]+fk[4]
if tp == "C" or tp == "S" and int(fph)<24 and int(fpm)<60 and int(fkh)<24 and int(fkm)<60:
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

    if round(v, 2)>140 and tp=="S":
        mandat="M"
    else:
        mandat="."
    if round(v, 2)>80 and tp=="C":
        mandat="M"
    else:
        mandat="."


    print(nr," ", mandat," ", round(v, 2),"km/h")
else:
    print("BLAD")


def vaqtni_sekundga_aylantirish(vaqt):
    soat, daqiqa, sekund = map(int, vaqt.split(':'))
    sekundlar = soat * 3600 + daqiqa * 60 + sekund
    return sekundlar

def farqni_hisoblash(vaqt1, vaqt2):
    sekundlar1 = vaqtni_sekundga_aylantirish(vaqt1)
    sekundlar2 = vaqtni_sekundga_aylantirish(vaqt2)
    farq = abs(sekundlar2 - sekundlar1)
    return farq
vaqt1 = input()
vaqt2 = input()

farq = farqni_hisoblash(vaqt1, vaqt2)
print("Ikki vaqt ko'rsatkichlari oralig'ida", farq, "sekund bor.")

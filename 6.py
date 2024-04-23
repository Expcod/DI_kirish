def tortburchak_kvadrat_emasligini_aniqlash(x1, y1, x2, y2, x3, y3, x4, y4):
    a = (x1 - x2) ** 2 + (y1 - y2) ** 2
    b = (x2 - x3) ** 2 + (y2 - y3) ** 2
    c = (x3 - x4) ** 2 + (y3 - y4) ** 2
    d = (x4 - x1) ** 2 + (y4 - y1) ** 2
    
    if a == b == c == d:
        return "To'rtburchak kvadrat"
    else:
        return "To'rtburchak kvadrat emas"

x1, y1 = 0, 0
x2, y2 = 0, 4
x3, y3 = 4, 4
x4, y4 = 4, 0

natija = tortburchak_kvadrat_emasligini_aniqlash(x1, y1, x2, y2, x3, y3, x4, y4)
print(natija)

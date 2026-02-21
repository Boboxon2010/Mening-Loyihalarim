def daraja_oshirish(a, b):
    return a ** b


def salomber_ism(ism):
    ism = ism.strip()
    if ism == "":
        return "Assalomu alaykum!"
    return "Assalomu alaykum, hurmatli " + ism.title()


def ishorani_aniqlash(son):
    if son > 0:
        return "Sonning ishorasi musbat +"
    elif son < 0:
        return "Sonning ishorasi manfiy -"
    else:
        return "Son 0 ga teng"


def mashina_taklif_qilish(summa):
    # input() bu yerda bo‘lmasin, qiymatni tashqaridan beramiz
    if summa > 50 and summa <= 100:
        return "Siz haydalgan Spark olishingiz mumkin."
    elif summa > 100 and summa < 160:
        return "Siz bu pulga Damas sotib olishingiz mumkin."
    elif summa >= 160 and summa < 250:
        return "Siz bu pulga yangi Cobalt olishingiz mumkin."
    elif summa >= 250 and summa < 500:
        return "Siz bu pulga yangi Tracker sotib olishingiz mumkin."
    else:
        return "Bu summa bilan mos taklif topilmadi."


def orta_arifmetik(*sonlar):
    if len(sonlar) == 0:
        return "Son kiritilmadi!"

    yigindi = 0
    for i in sonlar:
        yigindi += i

    return yigindi / len(sonlar)


def orta_geometrik(*sonlar):
    if len(sonlar) == 0:
        return "Son kiritilmadi!"

    jami = 1
    for i in sonlar:
        jami *= i

    # geometrik o‘rta: (jami)^(1/n)
    return jami ** (1 / len(sonlar))

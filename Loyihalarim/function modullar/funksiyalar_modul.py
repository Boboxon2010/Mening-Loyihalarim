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
def juftmi(son):
    """Son juft yoki toq ekanini aniqlaydi."""
    if son % 2 == 0:
        return "Juft son"
    else:
        return "Toq son"


def kattasini_top(a, b):
    """Ikki sondan kattasini qaytaradi."""
    if a > b:
        return a
    else:
        return b


def kichigini_top(a, b):
    """Ikki sondan kichigini qaytaradi."""
    if a < b:
        return a
    else:
        return b


def modul(son):
    """Sonning modulini qaytaradi."""
    if son < 0:
        return -son
    return son


def kvadrat(son):
    """Sonning kvadratini hisoblaydi."""
    return son * son


def kub(son):
    """Sonning kubini hisoblaydi."""
    return son * son * son


def faktorial(n):
    """n sonining faktorialini hisoblaydi."""
    if n < 0:
        return "Manfiy son uchun faktorial yo‘q!"
    natija = 1
    for i in range(1, n + 1):
        natija *= i
    return natija


def fibonacci(n):
    """Fibonacci ketma-ketligidan n ta element qaytaradi."""
    if n <= 0:
        return "n musbat bo‘lsin!"
    a = 0
    b = 1
    natija = []
    for i in range(n):
        natija.append(a)
        a, b = b, a + b
    return natija


def raqamlar_yigindisi(n):
    """Son raqamlarining yig‘indisini topadi."""
    n = abs(n)
    yigindi = 0
    while n > 0:
        yigindi += n % 10
        n //= 10
    return yigindi


def raqamlar_soni(n):
    """Son nechta raqamdan iboratligini aniqlaydi."""
    n = abs(n)
    if n == 0:
        return 1
    soni = 0
    while n > 0:
        soni += 1
        n //= 10
    return soni


def teskari_son(n):
    """Sonni teskari qilib qaytaradi."""
    manfiy = False
    if n < 0:
        manfiy = True
        n = -n
    yangi = 0
    while n > 0:
        yangi = yangi * 10 + n % 10
        n //= 10
    if manfiy:
        return -yangi
    return yangi


def palindrommi(n):
    """Son palindrom ekanini tekshiradi."""
    if n == teskari_son(n):
        return "Palindrom"
    else:
        return "Palindrom emas"


def min_top(*sonlar):
    """Berilgan sonlar ichidan eng kichigini topadi."""
    if len(sonlar) == 0:
        return "Son kiritilmadi!"
    eng_kichik = sonlar[0]
    for i in sonlar:
        if i < eng_kichik:
            eng_kichik = i
    return eng_kichik


def max_top(*sonlar):
    """Berilgan sonlar ichidan eng kattasini topadi."""
    if len(sonlar) == 0:
        return "Son kiritilmadi!"
    eng_katta = sonlar[0]
    for i in sonlar:
        if i > eng_katta:
            eng_katta = i
    return eng_katta


def qoldiq(a, b):
    """a ni b ga bo‘lgandagi qoldiqni qaytaradi."""
    if b == 0:
        return "0 ga bo‘lib bo‘lmaydi!"
    return a % b


def butun_bolish(a, b):
    """a ni b ga butun bo‘lish natijasini qaytaradi."""
    if b == 0:
        return "0 ga bo‘lib bo‘lmaydi!"
    return a // b


def foiz(summa, foiz):
    """Berilgan summaning foizini hisoblaydi."""
    return summa * foiz / 100


def chegirma(narx, foiz):
    """Narxdan foiz bo‘yicha chegirma hisoblaydi."""
    return narx - (narx * foiz / 100)


def boluvchilar(n):
    """Sonning barcha bo‘luvchilarini ro‘yxat qilib qaytaradi."""
    natija = []
    for i in range(1, n + 1):
        if n % i == 0:
            natija.append(i)
    return natija


def ekub(a, b):
    """Ikki sonning EKUB ini topadi."""
    while b != 0:
        a, b = b, a % b
    return a


def ekuk(a, b):
    """Ikki sonning EKUK ini topadi."""
    return a * b // ekub(a, b)


def temperaturani_aylantir(temp, tur):
    """Temperaturani C↔F ga aylantiradi. Turni kiritganda c_to_f yoki f_to_c qilib kiriting!"""
    if tur == "c_to_f":
        return temp * 9 / 5 + 32
    elif tur == "f_to_c":
        return (temp - 32) * 5 / 9
    else:
        return "Noto‘g‘ri tur"


def uchburchak_tekshir(a, b, c):
    """Tomonlar bo‘yicha uchburchak mavjudligini tekshiradi."""
    if a + b > c and a + c > b and b + c > a:
        return "Uchburchak bo‘ladi"
    else:
        return "Uchburchak bo‘lmaydi"


def aylana_yuzi(r):
    """Aylananing yuzini hisoblaydi."""
    if r < 0:
        return "Radius manfiy bo‘lmaydi!"
    return 3.14 * r * r


def matnni_tozala(matn):
    """Matn bosh va oxiridagi bo‘sh joylarni olib tashlaydi."""
    return matn.strip()
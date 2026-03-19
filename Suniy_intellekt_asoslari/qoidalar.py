import random
def qoidalar(s):
    a = []
    if 'hiragana' in s and 'katakana' in s and 'kanji' in s:
        a.append(1)
    if 'sakura_ramz' in s:
        a.append(2)
    if 'f1' in s and 'texnologik' in s:
        a.append(3)
    if 'mehnatkash' in s and 'intizimli' in s:
        a.append(4)
    if 'tinch_okeanida' in s:
        a.append(5)
    if 'osiyo' in s and 'orollar_davlati' in s:
        a.append(6)
    if 'iqtisodiy_rivojlangan' in s:
        a.append(7)
    if 'madaniyatli' in s and 'texnik' in s and 'g7' in s:
        a.append(8)
    if 'tabiatga_sigishili' in s:
        if 'sharq_etika' in s:
            if 'sharqiy_osiyo_davlati' in s:
                if 'g7' in s:
                    if 'toyota' in s:
                        a.append(9)
    if 'tokyo' in s:
        a.append(10)

    return a

def bajar(k, s):
    if k == 1:
        for x in ['hiragana', 'katakana', 'kanji']:
            s.remove(x)
        s.append('madaniyatli')
    if k == 2:
        s.remove('sakura_ramz'):
        s.append('tabiatga_sigishili')
    if k == 3:
        for x in ['f1', 'texnologik']:
            s.remove(x)
        s.append('texnik')
    if k == 4:
        for x in ['mehnatkash', 'intizimli']:
            s.remove(x)
        s.append('sharq_etika')
    if k == 5:
        s.remove('tinch_okeanida');
        s.append('orollar_davlati')
    if k == 6:
        for x in ['osiyo', 'orollar_davlati']:
            s.remove(x)
        s.append('sharqiy_osiyo_davlati')
    if k == 7:
        s.remove('iqtisodiy_rivojlangan');
        s.append('g7')
    if k == 8:
        for x in ['madaniyatli', 'texnik']:
            s.remove(x)
        s.append('toyota')
    if k == 9:
        for x in ['tabiatga_sigishili', 'sharq_etika', 'sharqiy_osiyo_davlati', 'g7', 'toyota']:
            s.remove(x)
        s.append('tokyo')
    if k == 10:
        s.remove('tokyo');
        s.append('Yaponiya')
    return s

if __name__ == "__main__":
    print("Boshlang'ich faktlarni kiriting (joy tashlab):")
    # malumot = input("> ").lower().split()
    s = ['hiragana','sakura_ramz','f1','texnologik','mehnatkash','intizimli','katakana','tinch_okeanida','osiyo','iqtisodiy_rivojlangan']
    karilatsiya = qoidalar(s)
    for i in range(len(karilatsiya)):
        random_natijasi = random.choice(karilatsiya)
        print(f"{random_natijasi}qoidaga kora bajardi {karilatsiya}")
        # bajardi = bajar(random_natijasi,s)
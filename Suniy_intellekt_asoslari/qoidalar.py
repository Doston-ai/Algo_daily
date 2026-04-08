def avtobus_ekspert_tizimi(faktlar):
    print(f"Boshlang'ich faktlar: {faktlar}\n")
    
    yangi_fakt_topildi = True
    while yangi_fakt_topildi:
        yangi_fakt_topildi = False
        
        # 11-QOIDA: Elektr -> Elektromobil
        if 'elektr' in faktlar and 'elektromobil' not in faktlar:
            faktlar.add('elektromobil')
            faktlar.remove('elektr') 
            print("[Qoida 11] Qo'llandi: Elektr -> Elektromobil")
            yangi_fakt_topildi = True

        # 6-QOIDA: Gaz -> Gazda yuruvchi
        if 'gaz' in faktlar and 'gazda_yuruvchi' not in faktlar:
            faktlar.add('gazda_yuruvchi')
            faktlar.remove('gaz')
            print("[Qoida 6] Qo'llandi: Gaz -> Gazda yuruvchi")
            yangi_fakt_topildi = True

        # 2-QOIDA: Yo'lovchi tashish + Shinam o'rindiqlar -> D toifa
        if 'yolovchi_tashish' in faktlar and 'shinam_orin' in faktlar and 'd_toifa' not in faktlar:
            faktlar.add('d_toifa')
            faktlar.remove('yolovchi_tashish')
            faktlar.remove('shinam_orin')
            print("[Qoida 2] Qo'llandi: Yo'lovchi tashish + Shinam o'rin -> D toifa")
            yangi_fakt_topildi = True

        # 5-QOIDA: Elektromobil + Gazda yuruvchi -> Gibrid
        if 'elektromobil' in faktlar and 'gazda_yuruvchi' in faktlar and 'gibrid' not in faktlar:
            faktlar.add('gibrid')
            faktlar.remove('elektromobil')
            faktlar.remove('gazda_yuruvchi')
            print("[Qoida 5] Qo'llandi: Elektromobil + Gazda yuruvchi -> Gibrid")
            yangi_fakt_topildi = True

        # 8-QOIDA: Gibrid + D toifa -> AVTOBUS
        if 'gibrid' in faktlar and 'd_toifa' in faktlar and 'avtobus' not in faktlar:
            faktlar.add('avtobus')
            faktlar.remove('gibrid')
            faktlar.remove('d_toifa')
            print("[Qoida 8] Qo'llandi: Gibrid + D toifa -> AVTOBUS")
            yangi_fakt_topildi = True

    return faktlar

# --- Tizimni ishga tushirish ---
# Siz bergan atributlar: Gaz, Yo'lovchi tashish, Elektr, Shinam_o'
boshlangich_bilimlar = {'gaz', 'yolovchi_tashish', 'elektr', 'shinam_orin'}

natija = avtobus_ekspert_tizimi(boshlangich_bilimlar)

if 'avtobus' in natija:
    print("\nNatija: Bu transport vositasi - AVTOBUS!")
else:
    print("\nNatija: Avtobus ekanligini aniqlash uchun yetarli faktlar topilmadi.")
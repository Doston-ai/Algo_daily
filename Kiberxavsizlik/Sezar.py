def sezar_shifrlash(matn, kalit):
    natija = ""
    
    for i in range(len(matn)):
        belgi = matn[i]
        
        # Katta harflarni shifrlash
        if belgi.isupper():
            natija += chr((ord(belgi) + kalit - 65) % 26 + 65)
        # Kichik harflarni shifrlash
        elif belgi.islower():
            natija += chr((ord(belgi) + kalit - 97) % 26 + 97)
        # Boshqa belgilarni (bo'shliq, belgi) o'zgarishsiz qoldirish
        else:
            natija += belgi

    return natija
def deshifrlash(matn, kalit):
    return sezar_shifrlash(matn, -kalit)
        


# Foydalanish:
xabar = "STARTAP"
k = 12
shifrlangan = sezar_shifrlash(xabar, k)
deshifrlangan = deshifrlash(shifrlangan, k)
print("Xabar:", xabar)
print(f"Shifrlangan matn: {shifrlangan}")
print("Deshifrangan matn:", deshifrlangan)


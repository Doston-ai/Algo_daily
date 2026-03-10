def vigenere_encrypt(text, key):
    """Vigenere shifri - matnni shifrlash"""
    result = ""
    key = key.upper()
    key_index = 0

    for char in text.upper():
        if char.isalpha():
            # Shift: kalit harfining pozitsiyasi
            shift = ord(key[key_index % len(key)]) - ord('A')
            # Shifrlangan harf
            encrypted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += encrypted
            key_index += 1
        else:
            result += char  # bo'shliq va boshqalar o'zgarmaydi

    return result


def vigenere_decrypt(text, key):
    """Vigenere shifri - matnni deshifrlash"""
    result = ""
    key = key.upper()
    key_index = 0

    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            # Teskari shift
            decrypted = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            result += decrypted
            key_index += 1
        else:
            result += char

    return result


def show_table(text, key):
    """Shifrlash jadvalini ko'rsatish"""
    key = key.upper()
    text = text.upper()
    key_index = 0

    print(f"\n{'Harf':<8} {'Kalit':<8} {'Shift':<8} {'Natija':<8}")
    print("-" * 35)

    for char in text:
        if char.isalpha():
            k = key[key_index % len(key)]
            shift = ord(k) - ord('A')
            encrypted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            print(f"{char:<8} {k:<8} {shift:<8} {encrypted:<8}")
            key_index += 1
        else:
            print(f"{char:<8} {'—':<8} {'—':<8} {char:<8}")


# ========== TEST ==========
text = "HELLO WORLD"
key = "KEY"

encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)

print(f"Asl matn    : {text}")
print(f"Kalit       : {key}")
print(f"Shifrlangan : {encrypted}")
print(f"Deshifrlangan: {decrypted}")

show_table(text, key)
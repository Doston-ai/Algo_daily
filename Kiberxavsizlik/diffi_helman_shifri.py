def dif_helm(p, g, a, b):
    A = g**a%p
    B = g**b%p
    Ka = B**a%p
    Kb = A**b%p
    if Ka == Kb:
        print("Kalitlar to'g'ri chiqdi")
    else:
        print("Xatolik ketdi")
    return f"A = {A}\nB = {B}\nKa = {Ka}\nKb = {Kb}"
print(dif_helm(97, 5, 18, 14))
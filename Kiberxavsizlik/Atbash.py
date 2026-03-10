# def atbash(text):
#     result=''
#     result2 = ""
#     for char in text.upper():
#         if char.isalpha():
#             result += chr(90-(ord(char) - 65))
#         else:
#             result += char
    
#     for matn, shifrlangan in zip(text, result):
#         if matn.isupper():
#             result2+=shifrlangan.upper()
#         else:
#             result2+=shifrlangan.lower()
#     return result2

# matn = input("Shifirlanuvchi matn kiriting\n>>> ")
# a = atbash(matn)
# print(f"Shifirlanuvchi matn: {matn}")
# print(f"Atbash shifrlash:  {a}")
# print(f"Atbash deshiflash: {atbash(a)}")




import tkinter as tk
from tkinter import messagebox

def atbash_logic(text):
    """Atbash shifrlash va deshifrlash algoritmi"""
    result = ""
    for char in text:
        if char.isalpha():
            # Katta harflar uchun (A=65, Z=90)
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            # Kichik harflar uchun (a=97, z=122)
            else:
                result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result

def process_text():
    input_text = entry_input.get()
    if not input_text:
        messagebox.showwarning("Xatolik", "Iltimos, matn kiriting!")
        return
    
    output_text = atbash_logic(input_text)
    label_result.config(text=output_text, fg="#3CB334")

# Asosiy oyna sozlamalari
root = tk.Tk()
root.title("Atbash Shifrator")
root.geometry("400x300")
root.configure(bg="#2c3e50")

# Sarlavha
lbl_title = tk.Label(root, text="Atbash Algoritmi", font=("Arial", 18, "bold"), 
                     bg="#2c3e50", fg="white")
lbl_title.pack(pady=15)

# Matn kiritish joyi
lbl_instruction = tk.Label(root, text="Matnni kiriting:", bg="#2c3e50", fg="#ecf0f1")
lbl_instruction.pack()

entry_input = tk.Entry(root, font=("Arial", 14), width=30)
entry_input.pack(pady=5)

# Tugma
btn_convert = tk.Button(root, text="Shifrlash", command=process_text,
                        bg="#3498db", fg="white", font=("Arial", 12, "bold"),
                        padx=10, pady=5, cursor="hand2")
btn_convert.pack(pady=20)

# Natija ko'rinadigan joy
lbl_res_title = tk.Label(root, text="Natija:", bg="#502c36", fg="#ecf0f1")
lbl_res_title.pack()

label_result = tk.Label(root, text="...", font=("Courier", 16, "bold"), 
                        bg="#2c3e50", fg="green", wraplength=350)
label_result.pack(pady=10)

root.mainloop()
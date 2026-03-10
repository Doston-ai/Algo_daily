from pprint import pprint 
import numpy as np
# qiziqishlari
student = [2, 4, 5]   # matematika, dasturlash, til

# Kitoblar
books = {
    "Matematika asoslari":        [5, 1, 0],
    "Oliy matematika":           [5, 0, 0],
    "Diskret matematika":        [5, 2, 0],
    "Ehtimollar nazariyasi":     [4, 1, 0],

    "Python dasturlash":         [1, 5, 0],
    "C++ dasturlash":            [3, 5, 0],
    "Algoritmlar va tuzilmalar": [4, 5, 0],
    "Ma'lumotlar bazasi (SQL)":  [2, 4, 0],
    "Web dasturlash":            [1, 4, 1],

    "Sun'iy intellekt":          [3, 5, 1],
    "Machine Learning":          [4, 5, 0],
    "Deep Learning":             [3, 5, 0],
    "Data Science":              [3, 5, 1],

    "Ingliz tili (Beginner)":    [0, 1, 5],
    "Ingliz tili (IELTS)":       [1, 0, 5],
    "Texnik ingliz tili":        [0, 0, 5],

    "Akademik yozuv":            [1, 1, 4],
    "Mantiq va tafakkur":        [4, 1, 1]
}


# Cosinus similarity funksiyasi
import math

def cosinus_similarity(a, b):
    # dot = sum(a[i] * b[i] for i in range(len(a)))
    dot = 0
    for i in range(len(a)):
        dot += a[i] * b[i]
        
        
    norm_a = math.sqrt(sum(x*x for x in a))
    norm_b = math.sqrt(sum(x*x for x in b))
    return dot / (norm_a * norm_b)

scores = {}

for book, score in books.items():
    oxshashlik = cosinus_similarity(student, score)
    scores[book] =  oxshashlik
# pprint(scores)

sorted_natijalar = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print('Qiziqishga eng mos kitob \n>>> ', sorted_natijalar[0][0], f': {sorted_natijalar[0][1]:.3f}')
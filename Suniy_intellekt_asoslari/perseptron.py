# import numpy as np

# class Perceptron:
#     def __init__(self, learning_rate=0.01, n_iters=1000):
#         self.lr = learning_rate
#         self.n_iters = n_iters
#         self.weights = None
#         self.bias = None

#     def fit(self, X, y):
#         n_samples, n_features = X.shape
#         # Vaznlarni noldan boshlaymiz
#         self.weights = np.zeros(n_features)
#         self.bias = 0

#         # O'qitish jarayoni
#         for _ in range(self.n_iters):
#             for idx, x_i in enumerate(X):
#                 # Chiziqli yig'indi: z = w*x + b
#                 linear_output = np.dot(x_i, self.weights) + self.bias
#                 # Faollashtirish (Heaviside step function)
#                 y_predicted = np.where(linear_output >= 0, 1, 0)

#                 # Vaznlarni yangilash (Perceptron o'qitish qoidasi)
#                 update = self.lr * (y[idx] - y_predicted)
#                 self.weights += update * x_i
#                 self.bias += update

#     def predict(self, X):
#         linear_output = np.dot(X, self.weights) + self.bias
#         y_predicted = np.where(linear_output >= 0, 1, 0)
#         return y_predicted

# # Test qilish uchun ma'lumotlar (Masalan, OR mantiqiy amali)
# if __name__ == "__main__":
#     X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
#     y = np.array([0, 1, 1, 1]) # OR natijalari

#     p = Perceptron(learning_rate=0.1, n_iters=10)
#     p.fit(X, y)
    
#     print(f"Bashorat: {p.predict(X)}")


# import numpy as np

# # 1. Model o'qib bo'lganidan keyin qolgan "aqlli" vaznlar
# weights = np.array([0.7, 0.5]) 
# bias = -0.8

# # 2. Yangi kelgan ma'lumot (Tarvuz: Yaltiroqlik=0.9, Ovoz=0.8)
# new_watermelon = np.array([0.9, 0.8])

# def predict_simple(x, w, b):
#     # Skalyar ko'paytma (dot product): (0.9*0.7) + (0.8*0.5)
#     z = np.dot(x, w) + b
    
#     print(f"Hisoblangan chiziqli yig'indi (z): {z:.2f}")
    
#     # Faollashtirish funksiyasi
#     if z >= 0:
#         return 1  # Pishgan
#     else:
#         return 0  # Xom

# # Bashoratni amalga oshiramiz
# result = predict_simple(new_watermelon, weights, bias)

# if result == 1:
#     print("Bashorat: Tarvuz pishgan! ✅")
# else:
#     print("Bashorat: Tarvuz hali xom. ❌")



import numpy as np

# 1. Kiruvchi ma'lumotlar (Input)
x = np.array([8, 4])

# 2. Vazn koeffitsientlari (Weights)
w = np.array([0.4, -0.6])

# 3. Og'ish koeffitsienti (Bias)
b = -1

# --- CHIZIQLI HISOBLASH (z) ---
# Formula: z = x1*w1 + x2*w2 + b
z = np.dot(x, w) + b

print(f"Chiziqli yig'indi (z): {z}")

# --- 1-VARIANT: ODDYI QAROR (Heaviside Step Function) ---
# Agar z 0 dan katta bo'lsa 1, aks holda 0
natija = 1 if z >= 0 else 0
print(f"Oddiy perceptron natijasi: {natija}")

# --- 2-VARIANT: SIGMOID FUNKSIYASI ---
# Bu ehtimollikni (0 va 1 oralig'idagi qiymatni) hisoblaydi
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

print(f"Sigmoid natijasi (ehtimollik): {sigmoid(z)}")
import numpy as np
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


#  Normallashtirish (Min-Max)
def normalize(X):
    return (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))


#  Masofa metrikalari
def euclidean(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def manhattan(p1, p2):
    return np.sum(np.abs(p1 - p2))

def chebyshev(p1, p2):
    return np.max(np.abs(p1 - p2))


#  KNN predict
def predict(X_train, y_train, X_test, k, distance_func):
    predictions = []
    for x in X_test:
        distances = [distance_func(x, x_train) for x_train in X_train]
        k_indices = np.argsort(distances)[:k]
        k_labels = [y_train[i] for i in k_indices]
        most_common = Counter(k_labels).most_common(1)[0][0]    # ({1: 3, 0: 2}) , [(1, 3)]
        predictions.append(most_common)

    return predictions


#  Accuracy
def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)*100


#  Eng yaxshi K ni topish
def find_best_k(X_train, y_train, X_test, y_test, distance_func, max_k=15):
    best_k = 1
    best_score = 0

    for k in range(1, max_k + 1):
        y_pred = predict(X_train, y_train, X_test, k, distance_func)
        score = accuracy(y_test, y_pred)
        print(f"k={k}, accuracy={score:.4f}")

        if score > best_score:
            best_score = score
            best_k = k

    print(f"\nEng yaxshi k = {best_k}, accuracy = {best_score:.4f}")
    return best_k


# --- Dataset yuklash ---
iris = load_iris()
X = iris.data
y = iris.target

# Train/Test bo‘lish
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)

# Normallashtirish
X_train = normalize(X_train)
X_test = normalize(X_test)

# 3 ta metrika bo'yicha tekshirish
print("=== Euclidean ===")
find_best_k(X_train, y_train, X_test, y_test, euclidean)

print("\n=== Manhattan ===")
find_best_k(X_train, y_train, X_test, y_test, manhattan)

print("\n=== Chebyshev ===")
find_best_k(X_train, y_train, X_test, y_test, chebyshev)

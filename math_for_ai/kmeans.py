import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import pprint 

def euclidean(point, data):
    data = np.array(data)
    return np.sqrt(np.sum((point - data)**2, axis=1))

class KMeans:
    def __init__(self, n_clusters=8, max_iter=10):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        self.markaz = [random.choice(X)]

        for _ in range(self.n_clusters-1):
            masofa = np.sum([euclidean(markaz, X) for markaz in self.markaz], axis=0)
            masofa /= np.sum(masofa)
            yangi_markaz_idx, = np.random.choice(range(len(X)), size=1, p=masofa)
            self.markaz += [X[yangi_markaz_idx]]

        iteration = 0
        oldingi_markazlar = None
        while np.not_equal(self.markaz, oldingi_markazlar).any() and iteration < self.max_iter:

            # self.guruhlar — har bir clusterning nuqtalari saqlanadi
            self.guruhlar = [[] for _ in range(self.n_clusters)]
            for a in X:
                masofa = euclidean(a, self.markaz)
                markaz_idx = np.argmin(masofa)
                self.guruhlar[markaz_idx].append(a)

            oldingi_markazlar = self.markaz
            self.markaz = [np.mean(clusters, axis=0) for clusters in self.guruhlar]

            for i, markaz in enumerate(self.markaz):
                if np.isnan(markaz).any():
                    self.markaz[i] = oldingi_markazlar[i]

            iteration += 1

    # def evaluate(self, X):
    #     markazlar = []
    #     markazlar_idxs = []
    #     for a in X:
    #         masofa = euclidean(a, self.markaz)
    #         markaz_idx = np.argmin(masofa)
    #         markazlar.append(self.markaz[markaz_idx])
    #         markazlar_idxs.append(markaz_idx)
    #     return markazlar, markazlar_idxs

    def plot(self):
        k = self.n_clusters
        colors = ['r', 'b', 'g', 'y', 'purple', 'orange', 'pink', 'cyan']

        plt.figure(figsize=(10, 10))

        for i, guruh in enumerate(self.guruhlar):
            xs = [p[0] for p in guruh]
            ys = [p[1] for p in guruh]
            plt.scatter(xs, ys, color=colors[i % len(colors)], label=f'Guruh {i+1}')

        for c in self.markaz:
            plt.scatter(c[0], c[1], color='k', s=200, marker='*')

        plt.title(f'K-means (k = {k})')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(alpha=0.4)
        plt.show()


# ── Ishlatish 

# np.random.seed(42)

# X = np.random.uniform(low=0, high=100, size=(300, 2))
X = pd.read_csv("D:\Projects\Algo_daily\math_for_ai\kmeans_2000_points.csv")
X = X.values

# random.seed(42)
kmeans = KMeans(n_clusters=4, max_iter=10)
kmeans.fit(X)

# markazlar, markaz_idxlar = kmeans.evaluate(X)
# pprint.pprint(markazlar)
# print(markaz_idxlar)

# chizma
kmeans.plot()

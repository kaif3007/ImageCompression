import numpy as np
import imageio
import scipy
from PIL import Image


def find_closest_centroids(X, centroids):
    m = X.shape[0]
    k = centroids.shape[0]
    idx = np.zeros(m)
    
    for i in range(m):
        min_dist = 1000000
        for j in range(k):
            dist = np.sum((X[i,:] - centroids[j,:]) ** 2)
            if dist < min_dist:
                min_dist = dist
                idx[i] = j
    
    return idx

def compute_centroids(X, idx, k):
    m, n = X.shape
    centroids = np.zeros((k, n))
    
    for i in range(k):
        indices = np.where(idx == i)
        centroids[i,:] = (np.sum(X[indices,:], axis=1) / len(indices[0])).ravel()
    
    return centroids

def run_k_means(X, initial_centroids, max_iters):
    m, n = X.shape
    k = initial_centroids.shape[0]
    idx = np.zeros(m)
    centroids = initial_centroids
    
    for i in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_centroids(X, idx, k)
    
    return idx, centroids

def init_centroids(X, k):
    m, n = X.shape
    centroids = np.zeros((k, n))
    idx = np.random.randint(0, m, k)
    
    for i in range(k):
        centroids[i,:] = X[idx[i],:]
    
    return centroids

def my_func(original,compressed,k):
    image = Image.open(original)
    newImage = image.resize((256,256))
    A = np.array(newImage)
    A = A / 255.

    X = np.reshape(A, (A.shape[0] * A.shape[1], A.shape[2]))
    initial_centroids = init_centroids(X,k)
    idx, centroids = run_k_means(X, initial_centroids, 10)
    idx = find_closest_centroids(X, centroids)
    X_recovered = centroids[idx.astype(int),:]
    X_recovered = np.reshape(X_recovered, (A.shape[0], A.shape[1], A.shape[2]))
    imageio.imwrite(compressed, X_recovered)

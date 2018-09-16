import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

#gettig data from image
image=ndimage.imread("houses.jpg")
plt.figure()
plt.imshow(image)
x, y, z =image.shape
X=image.reshape(x*y,z)(dtype=float64)

#inputs
print("provide the number of clusters:")
K=int(input())
print("provide the threshold value:")
e=float(input())

#initializing centroids
centeroids=[]
for i in range K:
  centeroids.append(X[][])

  

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage import io

url = "https://i.imgur.com/RArtpOd.png" #first image
img = io.imread(url)


print(img.shape)
img_init = img.copy()

plt.figure(figsize=(6, 6)) # plot initial image
plt.imshow(img_init)

img = img.reshape((img.shape[0] * img.shape[1],img.shape[2])) 
print(img.shape)

k = 5
clt = KMeans(n_clusters = k) # "pick out" the K-means tool from our collection of algorithms
clt.fit(img) # apply the model to our data, the image

print(clt.labels_)

label_indx = np.arange(0,len(np.unique(clt.labels_)) + 1) 

(hist, _) = np.histogram(clt.labels_, bins = label_indx) # count the number of pixels in each cluster
hist = hist.astype("float") # convert to float
hist /= hist.sum() # normalize the histogram
print(hist)

hist_bar = np.zeros((50, 300, 3), dtype = "uint8")
startX = 0
for (percent, color) in zip(hist,  clt.cluster_centers_): 
  endX = startX + (percent * 300) # to match grid
  cv2.rectangle(hist_bar, (int(startX), 0), (int(endX), 50),
      color.astype("uint8").tolist(), -1)
  startX = endX
 

plt.figure(figsize=(10, 10))
plt.subplot(121)
plt.imshow(img_init)
plt.subplot(122)
plt.imshow(hist_bar)
plt.show()

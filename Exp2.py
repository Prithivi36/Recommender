import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import cv2

image =cv2.cvtColor(cv2.imread("image.png"),cv2.COLOR_BGR2RGB)

blue,green,red = cv2.split(image)

df_blue = blue/255
pca_b=PCA(n_components=50)
pca_b.fit(df_blue)
trans_pca_b = pca_b.transform(df_blue)
b_arr=pca_b.inverse_transform(trans_pca_b)

df_green = green/255
pca_g=PCA(n_components=50)
pca_g.fit(df_green)
trans_pca_g = pca_g.transform(df_green)
g_arr=pca_g.inverse_transform(trans_pca_g)

df_red = red/255
pca_r=PCA(n_components=50)
pca_r.fit(df_red)
trans_pca_r = pca_r.transform(df_red)
r_arr=pca_r.inverse_transform(trans_pca_r)

imgRed = cv2.merge([b_arr,g_arr,r_arr])
plt.title("PCA Image")
plt.imshow(imgRed)
plt.show()
plt.title("Original Image")
plt.imshow(image)
plt.show()
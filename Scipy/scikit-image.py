from skimage import data, color, io
from skimage.transform import rescale, resize, downscale_local_mean
import matplotlib.pyplot as plt

#  pip install -U scikit-image

image = color.rgb2gray(io.imread('MachineLearning/center.jpg'))

image_rescaled = rescale(image, 0.25, anti_aliasing=False)
image_resized = resize(image, (image.shape[0] // 4, image.shape[1] // 4),
                       anti_aliasing=True)
image_downscaled = downscale_local_mean(image, (4, 3))
plt.figure(figsize=(20, 20))
plt.subplot(221), plt.imshow(image, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(image_rescaled,
                             cmap='gray'), plt.title('Rescaled')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(image_resized, cmap='gray'), plt.title('Resized')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(image_downscaled,
                             cmap='gray'), plt.title('Downscaled')
plt.xticks([]), plt.yticks([])
plt.show()

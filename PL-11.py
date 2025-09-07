import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Your image path
image_path = r'C:\Users\LENOVO\Pictures\Screenshots\Screenshot 2025-09-01 144352.png'

# Load the image
img = Image.open(image_path)
img_array = np.array(img)


print("Image Dimensions:", img_array.shape[0], "x", img_array.shape[1])
print("Image Shape:", img_array.shape)

if len(img_array.shape) == 3:
    print("Minimum Pixel Value in Blue Channel:", img_array[:, :, 2].min())
else:
    print("This is a grayscale image.")



#post lab b

img = Image.open(r'C:\Users\LENOVO\Pictures\Screenshots\Screenshot 2025-09-01 144352.png')
padded_img = ImageOps.expand(img, border=70, fill='black')

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(padded_img)
plt.title('Padded Image (Black Border)')
plt.axis('off')

plt.tight_layout()
plt.show()


#post lab- c

img = Image.open(r'C:\Users\LENOVO\Pictures\Screenshots\Screenshot 2025-09-01 144352.png')
img_array = np.array(img)

red = img_array[:, :, 0]
green = img_array[:, :, 1]
blue = img_array[:, :, 2]

plt.figure(figsize=(15, 5)plt.subplot(1, 3, 1)
plt.imshow(red, cmap='Reds')
plt.title('Red Channel')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(green, cmap='Greens')
plt.title('Green Channel')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(blue, cmap='Blues')
plt.title('Blue Channel')
plt.axis('off')

plt.tight_layout()
plt.show()

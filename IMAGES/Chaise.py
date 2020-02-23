#Importation des modules de traitement d'image
import cv2
from skimage import io
from scipy import ndimage

#On charge toutes les images de chaises
ImageCollection1 = io.ImageCollection("CHAISE/*.jpg", 0)

i = 0

#Redimensionnement et filtering des images (chaises et portes)
for chaise in ImageCollection1:
    chaise_resize = cv2.resize(chaise, (int(chaise.shape[1]//10), int(chaise.shape[0]//10)))

    chaise_filter = ndimage.uniform_filter(chaise_resize, size=2)

    cv2.imwrite(f'Images/Chaise/chaise{i}.png', chaise_filter)
    i += 1
print(f"\nTaille des chaises : {chaise.shape}")
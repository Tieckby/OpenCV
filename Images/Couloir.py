#Importation des modules de traitement d'image
import cv2
from skimage import io
from scipy import ndimage

#On charge toutes les images de couloirs
ImageCollection2 = io.ImageCollection("COULOIR/*.jpg", 0)

i = 0

for couloir in ImageCollection2:
    couloir_resize = cv2.resize(couloir, (int(couloir.shape[1]//10), int(couloir.shape[0]//15)))

    couloir_filter = ndimage.uniform_filter(couloir_resize, size=2)


    if couloir_filter.any() < 50:
        couloir_filter[couloir_filter < 50] = 0
    else:
        couloir_filter[couloir_filter] = 255

    cv2.imwrite(f'Images/Couloir/couloir{i}.png', couloir_filter)
    i += 1
print(f"\nTaille des couloirs : {couloir.shape}")
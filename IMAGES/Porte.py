#Importation des modules de traitement d'image
import cv2
from skimage import io
from scipy import ndimage

#On charge toutes les images de portes
ImageCollection2 = io.ImageCollection("PORTE/*.jpg", 0)

i = 0

for porte in ImageCollection2:
    porte_resize = cv2.resize(porte, (int(porte.shape[1]//10), int(porte.shape[0]//10)))

    porte_filter = ndimage.uniform_filter(porte_resize, size=2)

    cv2.imwrite(f'Images/Porte/porte{i}.png', porte_filter)
    i += 1
print(f"\nTaille des portes : {porte.shape}")
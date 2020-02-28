#Importation des modules de traitement d'image
import cv2
from skimage import io
from scipy import ndimage

#On charge toutes les images de tables
ImageCollection2 = io.ImageCollection("TABLE/*.jpg", 0)

i = 0

for table in ImageCollection2:
    table_resize = cv2.resize(table, (int(table.shape[1]//10), int(table.shape[0]//15)))

    table_filter = ndimage.uniform_filter(table_resize, size=2)

    if table_filter.any() < 50:
        table_filter[table_filter < 50] = 0
    else:
        table_filter[table_filter] = 255

    cv2.imwrite(f'Images/Table/table{i}.png', table_filter)
    i += 1
print(f"\nTaille des tables : {table.shape}")
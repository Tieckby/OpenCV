import cv2, time, pandas
from datetime import datetime
import matplotlib.pyplot as plt

#______________________________Process Image___________________________
# #Charge une image
# img = cv2.imread("plane.png", 1)

# #Type et taille de cet image
# h = img.shape[0]
# w = img.shape[1]
# print(f"Type : {type(img)}\nTaille : {img.shape}")
# print(f"\nHauteur = {h}, Largeur = {w}")

# img1 = cv2.resize(img, (400, 200))
# cv2.imshow("L'image redimensionnée", img1)

# cv2.imshow("Photo d'un avion", img) #Affiche l'image avec un titre
# cv2.waitKey(0) #Or cv2.waitKey(3000) -> Attend 3s (3000 milliseconde) pour quitter

# cv2.destroyAllWindows() #Ferme (détruit) la fenêtre apres le temps en milliseconde

# #_____________________________FaceDetection__________________________
# face_cascade = cv2.CascadeClassifier("haar_cascade_files/haarcascade_frontalface_alt.xml")
# img = cv2.imread("yaya.jpg", 1)

# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.5, minNeighbors=5)

# for x, y, w, h in faces:
#     img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

# resized = cv2.resize(img, (800, 700))

# cv2.imshow("Tiémoko", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#_______________________________Human detection_____________________________
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

img = cv2.imread("yaya.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

boxes, weights = hog.detectMultiScale(img, winStride=(5, 5))

for x, y, w, h in boxes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

resized = cv2.resize(img, (600, 600))

cv2.imshow("Tiémoko", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# #_______________________VideoCamera Detecttion_________________________
# face_cascade = cv2.CascadeClassifier("haar_cascade_files/haarcascade_frontalface_alt.xml")
# body_cascade = cv2.CascadeClassifier("haar_cascade_files/haarcascade_fullbody.xml")
# video = cv2.VideoCapture(0)

# if video.isOpened() == False:
#     print("Erreur d'ouverture de la camera ...")
# else:
#     i = 1
#     video_Launch = True

#     while video_Launch:
#         i += 1
#         ret, image = video.read()

#         face = face_cascade.detectMultiScale(image, scaleFactor=1.5, minNeighbors=5)
#         body = body_cascade.detectMultiScale(image, scaleFactor=1.5, minNeighbors=4)

#         # cv2.rectangle(image, start_point, end_point, color, thickness) : thickness->L'epaisseur de la ligne de bordure du rectangle en pixel
#         for x, y, w, h in face:
#             cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#             name = "Tiemoko"
#             font_name = cv2.FONT_HERSHEY_SIMPLEX
#             color = (255, 255, 255)
#             cv2.putText(image, name, (x, y-10), font_name, 1, color, 2, cv2.LINE_AA)

#         for x, y, w, h in body:
#            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 2)

#         cv2.imshow('Capture', image) #Affiche la videoCam
#         key = cv2.waitKey(1)

#         if key == ord('q'):
#             video_Launch = False

#     print(f"\nLe nombre d'image est {i}")
#     video.release() #Libère les ressources utilisées
#     cv2.destroyAllWindows() #Ferme tous les frames
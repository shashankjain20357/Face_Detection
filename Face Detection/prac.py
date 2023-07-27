import cv2
cap = cv2.VideoCapture(0)
facecascade = cv2.CascadeClassifier('lbpcascade_frontalface_improved.xml')
while (True):
    frame = cap.read()

from picamera2 import Picamera2
from time import sleep
import cv2

camera = Picamera2()
camera.start()

detector = cv2.QRCodeDetector()

while True:
    sleep(0.25)
    img = camera.capture_array()
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        print("data found! ", data)

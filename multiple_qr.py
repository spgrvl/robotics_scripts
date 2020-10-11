import pyzbar.pyzbar as pyzbar
import cv2

detected_qr = -1
qr_set = set()

cap = cv2.VideoCapture(0)

while(detected_qr != 4):
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decoded_obj = pyzbar.decode(img)
    detected_qr = len(decoded_obj)
    if detected_qr != 0:
        print(detected_qr)

for qr in decoded_obj:
    qr_set.add(qr.data.decode("utf-8"))

with open("qr.txt", 'w') as f:
    for qr in qr_set:
        f.write(qr + "\n")

cap.release()

print(qr_set)
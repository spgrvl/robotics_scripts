import pyzbar.pyzbar as pyzbar
import cv2

detected_qr = -1
cap = cv2.VideoCapture(0)

while(detected_qr != 4):
    ret, frame = cap.read()
    img = cv2.cvtColor(np.array(frame), cv2.COLOR_BGR2GRAY)
    decoded_obj = pyzbar.decode(img)
    detected_qr = len(decoded_obj)
    if detected_qr != 0:
        print(detected_qr)

cap.release()

for qr in decoded_obj:
    print(qr.data)
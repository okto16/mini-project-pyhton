import cv2

droidcam_url = "http://192.168.1.105:4747/video"
cap = cv2.VideoCapture(droidcam_url)

while True:
    ret, frame = cap.read()
    cv2.imshow("Scan Document", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

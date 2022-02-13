import cv2

camera = cv2.VideoCapture(0)
algTreinado = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    captura, frame = camera.read()
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detecta = algTreinado.detectMultiScale(cinza)
    for ( x, y, l, a ) in detecta:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (0,255,0),2)
        
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()



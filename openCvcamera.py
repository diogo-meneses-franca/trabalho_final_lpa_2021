import cv2

imagem = cv2.VideoCapture(0)
while (True):
    retorno, frame = imagem.read()
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break

imagem.release()
cv2.destroyAllWindows()

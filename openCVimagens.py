import cv2
#CARREGANDO UMA IMAGEM E REDIMENCIONANDO
imagem = cv2.imread("pessoas faces.jpg")
redimencionada = cv2.resize(imagem, (600,400))
cv2.imshow("Faces", redimencionada)
cv2.waitKey(0)

#MUDANDO A ESCALA DE COR
redi_cinza = cv2.cvtColor(redimencionada, cv2.COLOR_BGR2GRAY)
cv2.imshow("cinza", redi_cinza)
cv2.waitKey(0)

#UNINDO IMAGENS

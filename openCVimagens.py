import cv2
import matplotlib.pyplot as plt
import numpy as np
#CARREGANDO UMA IMAGEM E REDIMENCIONANDO
imagem = cv2.imread("pessoas faces.jpg",0)
#coresReversas = imagem[:,:, ::-1]
redimencionada = cv2.resize(imagem, (400,300))
#APRESENTANDO TODAS AS ESCALAS DE COR DA OPENCV
#escalasDeCor = cv2.cvtColor(imagem,cv2.COLOR_BGR2YCR_CB)
#COMO MOSTRAR A IMAGEM NA TELA COM AS DUAS BIBLIOTECAS OPENCV E MATPLOTLIB
cv2.imshow("Faces", redimencionada)
cv2.waitKey(0)
#plt.imshow(coresReversas)
#plt.waitforbuttonpress()

#MOSTRA A MATRIZ DA IMAGEM
#print(redimencionada)


#MOSTRA O TAMANHO DA IMAGEM
#print("Tamanho da imagem:", redimencionada.shape)
#print("Tipo de dado da imagem:", redimencionada.dtype)
#plt.imshow(coresReversas)
#plt.waitforbuttonpress()


#SALVANDO A IMAGEM
cv2.imwrite("imagemCinza.jpg", redimencionada)
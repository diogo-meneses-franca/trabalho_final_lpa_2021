import cv2
import matplotlib.pyplot as plt
import numpy as np
#CARREGANDO UMA IMAGEM E REDIMENCIONANDO
imagem = cv2.imread("pessoas faces.jpg",0)
#coresReversas = imagem[:,:, ::-1]
#redimencionada = cv2.resize(imagem, (1366,768))
#cv2.imshow("Faces", imagem)
#cv2.waitKey(0)
plt.imshow(imagem)
plt.waitforbuttonpress()
#MOSTRA A MATRIZ DA IMAGEM
#print(imagem)


#MOSTRA O TAMANHO DA IMAGEM
print("Tamanho da imagem:", imagem.shape)
print("Tipo de dado da imagem:", imagem.dtype)
#plt.imshow(coresReversas)
#plt.waitforbuttonpress()

#SEPARANDO A IMAGEM EM ESCALAS DE CORES
"""b,g,r = cv2.split(redimencionada)
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(r,cmap = 'gray'); plt.title("Vermelha")
plt.subplot(142);plt.imshow(g,cmap = 'gray'); plt.title("Verde")
plt.subplot(143);plt.imshow(b,cmap = 'gray'); plt.title("Azul")
misturada = cv2.merge((b,g,r))
plt.subplot(144);plt.imshow(misturada[:,:,::-1]),plt.title("Fundidas")
plt.waitforbuttonpress()"""

#SALVANDO A IMAGEM
#cv2.imwrite("imagemCinza.jpg", redimencionada)
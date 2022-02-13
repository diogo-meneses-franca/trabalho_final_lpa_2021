import cv2
import matplotlib.pyplot as plt
"""#CARREGANDO UMA IMAGEM E REDIMENCIONANDO
imagem = cv2.imread("pessoas faces.jpg",cv2.IMREAD_COLOR)
coresReversas = imagem[:,:, ::-1]
redimencionada = cv2.resize(imagem, (400,300))
#APRESENTANDO TODAS AS ESCALAS DE COR DA OPENCV
escalasDeCor = cv2.cvtColor(imagem,cv2.COLOR_BGR2YCR_CB)
#COMO MOSTRAR A IMAGEM NA TELA COM AS DUAS BIBLIOTECAS OPENCV E MATPLOTLIB
#cv2.imshow("Faces", redimencionada)
#cv2.waitKey(0)
plt.imshow(coresReversas)
plt.waitforbuttonpress()"""

#MOSTRA A MATRIZ DA IMAGEM
"""pequena = cv2.imread('imagem18x18.png',0)
plt.imshow(pequena, cmap = 'gray')
print(pequena)"""



#MOSTRA O TAMANHO DA IMAGEM
#print("Tamanho da imagem:", redimencionada.shape)
#print("Tipo de dado da imagem:", redimencionada.dtype)

#CORTANDO UMA IMAGEM
"""barquinho_bgr = cv2.imread('barquinho.jpg', cv2.IMREAD_COLOR)
barquinho_rgb = barquinho_bgr[:,:, ::-1]
cortada = barquinho_rgb[200:400, 300:600]
plt.imshow(cortada)
plt.waitforbuttonpress(0)"""


#UNINDO IMAGENS DIFERENTES
"""frente = cv2.imread('frente.jpg')
fundo = cv2.imread('fundo.jpg')
frente_red = cv2.resize(frente,(1366,768), interpolation= cv2.INTER_AREA)
fundo_red = cv2.resize(fundo,(1366,768), interpolation= cv2.INTER_AREA)
fusao = cv2.addWeighted(fundo_red, 0.5, frente_red, 0.8, 0.0)
cv2.imshow("Juntas", fusao)
cv2.waitKey(0)"""



#SALVANDO A IMAGEM
#cv2.imwrite("imagemCinza.jpg", redimencionada)
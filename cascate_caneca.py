import cv2

imagem = cv2.imread('Imagens teste canecas/teste01.png')

classificador = cv2.CascadeClassifier('haarcascade_caneca.xml')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemCinza)

print(deteccoes)
print(len(deteccoes))

for (x, y, l, a) in deteccoes:
    cv2.rectangle(imagem, (x,y), (x + l, y + a), (0,255,0), 2)

cv2.imshow('Detector de Canecas', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
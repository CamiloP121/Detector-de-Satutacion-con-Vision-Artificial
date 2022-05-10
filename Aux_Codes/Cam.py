'''
04/05/2022
Camilo Perez
Entorno: Env_SpO2
'''
## Librerias
import cv2
import pytesseract as tsc 
tsc.pytesseract.tesseract_cmd = r'C:\Users\perez\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
# Scripts Auxiliares
from Aux_Codes.Process import Spo2_Detec

def Detec(img):
    Num = tsc.image_to_string(img,
            config='--psm 10 --oem 3 -c tessedit_char_whitelist=1234567890') # Aplicar pytesseract
    Num = str(Num)
    print(Num)
    if Num != '' and len(Num) == 3:
        Text = 'Blood saturation is ' + Num
    else: Text = 'Loading'
    return Text

## Objeto Video Camara
class Cam:
    def __init__(self):
        self.cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.Haar = cv2.CascadeClassifier(r'records/cascade_3.xml')
        self.scale = 50
        self.minBords = 200
        self.minSize = (60,60)

    def open_cam(self,Show = False):
        Vec_frame = []
        while True:
            _,frame = self.cam.read()
            frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
            Vec_frame.append(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            Sp = self.Haar.detectMultiScale(gray,
            scaleFactor = 20,
            minNeighbors = 200,
            minSize=(60,40))
            imAux = frame.copy()
            if len(Sp) != 0:
                x,y,w,h = Sp[0]
                objeto = imAux[y-30:y+120,x-30:x+80] # [x1,y1],[x2,y2]

                if Show == True:
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    cv2.putText(frame,'SpO2',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
                    cv2.imshow('frame',frame)
                    cv2.imshow('frame2',objeto)
                    if cv2.waitKey(25) == ord('k'):
                        break


                Text = Detec(objeto)
                return Text
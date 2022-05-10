'''
04/05/2022
Camilo Perez
Entorno: Env_SpO2
'''
## Librerias
import time
import pyttsx3
from playsound import playsound
import os
# Scripts Adiionales
from Aux_Codes.Cam import Cam
## Funciones
# Iniciadores necesarios
def Star():
    Obj_Cam = Cam()
    Voice = pyttsx3.init()
    path = os.getcwd()
    # Indicacion de espera al usurio
    Text = ('Se tomora su Saturacion,',
            'espere 1 minuto mientras inicia')
    Voice.say(Text)
    Voice.runAndWait()
    # Si quieres que solo haga un conteo
    for i in range(3):
        time.sleep(10)
        Text = str((i+1)*10)+'seconds'
        Voice.say(Text)
        Voice.runAndWait()
    # Si quieres con musica
    '''path = os.getcwd() + r'/records/espera_30seg.wav'
    playsound(path)'''
    return Obj_Cam,Voice
# Despliegue menu aplicacion
if __name__ == '__main__':
    [Obj_Cam,Voice] = Star()
    # tiempo maximo 2 min
    inicio = time.time()
    while True:
        txt = Obj_Cam.open_cam()
        Voice.say(txt)
        Voice.runAndWait()
        time.sleep(2)
        fin = time.time()
        if  fin - inicio > 2*60:
            Text = 'Ending program. Thank you'
            Voice.say(Text)
            Voice.runAndWait()
            break
    Obj_Cam.release()
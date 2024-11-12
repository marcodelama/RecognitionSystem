import cv2
import face_recognition as fr
import numpy as np
import mediapipe as mp
import os
from tkinter import *
from PIL import Image, ImageTk
import imutils
import math

def Log():
  print("Hola Sing in")

def Sign():
  global RegName, RegUser, RegPassword, InputNameReg, InputUserReg, InputPasswordReg, cap, lblVideo, pantalla2
  # Extracción de datos: Name - User - Password
  RegName, RegUser, RegPassword = InputNameReg.get(), InputUserReg.get(), InputPasswordReg.get()

  #Formulario incompleto
  if len(RegName) == 0 or len(RegUser) == 0 or len(RegPassword) == 0:
    print("Formulario incompleto")
  else:
    #Validar usuarios
    UserList = os.listdir(OutFolderPathUser)

#Rutas
OutFolderPathUser = 'C:/Users/usuario/Desktop/Marco/RecognitionSystem/Database/Users'
PathUserCheck = 'C:/Users/usuario/Desktop/Marco/RecognitionSystem/Database/Users/'
OutlFolderPathFace = 'C:/Users/usuario/Desktop/Marco/RecognitionSystem/Database/Faces'

#Lista de información
info = []

#Ventana principal
pantalla = Tk()
pantalla.title("FACE RECOGNITION")
pantalla.geometry("1280x720")

#Fondo
imagenF = PhotoImage(file='C:/Users/usuario/Desktop/Marco/RecognitionSystem/SetUp/Inicio.png')
background = Label(image = imagenF, text="Inicio")
background.place(x=0, y=0, relheight=1, relwidth=1)

#Entradas de texto
InputNameReg = Entry(pantalla)
InputNameReg.place(x=110, y=320)

InputUserReg = Entry(pantalla)
InputUserReg.place(x=110, y=430)

InputPasswordReg = Entry(pantalla)
InputPasswordReg.place(x=110, y=540)

#Inicio de sesión
InputUserLog = Entry(pantalla)
InputUserLog.place(x=750, y=380)

InputPasswordLog = Entry(pantalla)
InputPasswordLog.place(x=750, y=500)

#Botones
#Registro
imagenBR = PhotoImage(file='C:/Users/usuario/Desktop/Marco/RecognitionSystem/SetUp/BtLogin.png')
BtReg = Button(pantalla, text="Registro", image=imagenBR,  height="40", width="200", command=Sign())
BtReg.place(x=300, y=580)

#Inicio
imagenBI = PhotoImage(file='C:/Users/usuario/Desktop/Marco/RecognitionSystem/SetUp/BtSign.png')
BtInicio = Button(pantalla, text="Registro", image=imagenBI,  height="40", width="200", command=Log())
BtInicio.place(x=900, y=580)

pantalla.mainloop()
"Converter with PySimpleGUI"
"this code have not any licence"
import PySimpleGUI as sg

layout = [[sg.Input(key="-INPUT-", size=(40, 40)),
          sg.Spin(["kilometer to meter", "meter to decimeter", "dosimeter to centimeter"], background_color="black", text_color="white", key="-SPIN-"),
           sg.Button("convert", key="-CONVERT-", button_color="black")],
          [sg.Text("output", key="-OUTPUT-", background_color = "white", text_color="black")]]

window = sg.Window("converter", layout, background_color="white", size=(500, 100))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
window.close()


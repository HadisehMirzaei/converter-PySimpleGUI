"Converter with PySimpleGUI"

import PySimpleGUI as sg

layout = [[sg.Input(key="-INPUT-", size=(40, 40)),
          sg.Spin(["kilometer to meter", "meter to decimeter", "dosimeter to centimeter"], background_color="black", text_color="white", key="-SPIN-"),
           sg.Button("convert", key="-CONVERT-", button_color="black")],
          [sg.Text("output", key="-OUTPUT-", background_color="white", text_color="black")]]

window = sg.Window("converter", layout, background_color="white", size=(500, 100))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-CONVERT-":
        input_number = values["-INPUT-"]
        if input_number.isnumeric():
            if values["-SPIN-"] == "kilometer to meter":
                output = round(float(input_number) * 1000, 2)
                output_str = f"{input_number} km is {output}m"
            if values["-SPIN-"] == "meter to decimeter":
                output = round(float(input_number) * 10, 2)
                output_str = f"{input_number} m is {output}dm"
            if values["-SPIN-"] == "dosimeter to centimeter":
                output = round(float(input_number) * 10, 2)
                output_str = f"{input_number} dm is {output}cm"
            window["-OUTPUT-"].update(output_str)
        else:
            window["-OUTPUT-"].update("please enter a number!!!!!!!!!!!!!!!!         not a text!")

window.close()


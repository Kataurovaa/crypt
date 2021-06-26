from tkinter import *
import tkinter as tk
from tkinter import messagebox



def start():
    def decrypt():
        def exit():
            for i in widgets_crypte:
                i.place_forget()
            start(flag)

        for i in widgets_main:
            i.place_forget()
        widgets_main.clear()

        flag = 1
        widgets_crypte = []

        label_greet = Label(text = "Выберите файл с\nзашифрованным сообщением", justify=CENTER, font="Verdana 14")
        label_greet.place(x = 100, y = 200)
        widgets_crypte.append(label_greet)

        button_enter = Button(text = "Выбрать", command = open_file)
        button_enter.place(x = 150, y = 50)
        widgets_crypte.append(button_enter)

        button_exit = Button(text = "Вернуться назад", command = exit)
        button_exit.place(x = 100, y = 300)
        widgets_crypte.append(button_exit)
    root = Tk()
    root.resizable(width=False, height=False)
    field = Canvas(root, width=500, height=500, bg='white')
    field.pack()

    widgets_main = []

    greeting = Label(text = "Добро пожаловать в шифровальщик.\nВы хотите:", justify=CENTER, font="Verdana 14")
    greeting.place(x = 100, y = 200)
    widgets_main.append(greeting)

    button_encrypt = Button(command = encrypt, text = "Зашифровать", width = 20, height = 10)
    button_encrypt.place(x = 200, y = 300)
    widgets_main.append(button_encrypt)

    button_decrypt = Button(command = decrypt, text = "Расшифровать", width = 20, height = 10)
    button_decrypt.place(x = 200, y = 400)
    widgets_main.append(button_decrypt)

    root.mainloop()




def to_10(inp, osn):
    p = 0
    digit = 0
    for i in range(len(inp)-1, -1, -1):
        tmp = ord(inp[i])
        if tmp >= 65:
            digit += (tmp-55) * osn**p
        else:
            digit += (tmp-48) * osn**p
        p += 1
    return digit

def from_10(inp, osn):
    digit = ""
    while inp > 0:
        tmp = inp % osn
        if tmp > 9:
            digit += str(chr(tmp+55))
        else:
            digit += str(tmp)
        inp //= osn
    return digit[::-1]

start()
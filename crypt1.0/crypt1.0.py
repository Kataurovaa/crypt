from tkinter import *
import tkinter as tk
from tkinter import messagebox



def start():
    def decrypt():
        def exit():
            for i in widgets_crypte:
                i.place_forget()
            start(flag)

        def open_file():
            de_colors = []
            input_file = easygui.fileopenbox(filetypes=["*.png"])
            image = Image.open(input_file)  # Открываем изображение
            draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
            width = image.size[0]  # Определяем ширину
            height = image.size[1]  # Определяем высоту
            pix = image.load()
            for y in range(0, height,60):
                for x in range(0, width, 60):
                    s = ""
                    r = pix[x+5, y][0] #узнаём значение красного цвета пикселя
                    t = from_10(r, 16)
                    s += "0"*(2-len(t))+t

                    g = pix[x+5, y][1] #зелёного
                    t = from_10(g, 16)
                    s += "0"*(2-len(t))+t

                    b = pix[x+5, y][2] #синего
                    t = from_10(b, 16)
                    s += "0"*(2-len(t))+t
                    if s == "FFFFFF":
                        break
                    de_colors.append(s)
            txt = color_to_text(de_colors)
            for j in range(len(txt)//37+1):
                answer = Label(text = txt[j*38:38+38*j], font = "Verdana 12", bg = 'white')
                answer.place(x= 35, y = 240 + 20*j)
                widgets_crypte.append(answer)

        def color_to_text(colors):
            tmp = ""
            for i in colors:
                tmp += i
            d = to_10(tmp, 16)
            res = from_10(d, 36)
            return res

        for i in widgets_main:
            i.place_forget()
        widgets_main.clear()

        flag = 1
        widgets_crypte = []

        label_greet = Label(text = "Выберите файл с\nзашифрованным сообщением", justify=CENTER, font="Verdana 14", bg = 'white')
        label_greet.place(x = 100, y = 50)
        widgets_crypte.append(label_greet)

        button_enter = Button(text = "Выбрать", command = open_file, width = 30, height = 3)
        button_enter.place(x = 135, y = 150)
        widgets_crypte.append(button_enter)

        button_exit = Button(text = "Вернуться назад", command = exit)
        button_exit.place(x = 380, y = 460)
        widgets_crypte.append(button_exit)

    root = Tk()
    root.resizable(width=False, height=False)
    field = Canvas(root, width=500, height=500, bg='white')
    field.pack()

    widgets_main = []

    greeting = Label(text = "����� ���������� � ������������.\n�� ������:", justify=CENTER, font="Verdana 14")
    greeting.place(x = 100, y = 200)
    widgets_main.append(greeting)

    button_encrypt = Button(command = encrypt, text = "�����������", width = 20, height = 10)
    button_encrypt.place(x = 200, y = 300)
    widgets_main.append(button_encrypt)

    button_decrypt = Button(command = decrypt, text = "������������", width = 20, height = 10)
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
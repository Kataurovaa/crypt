from tkinter import *
import tkinter as tk
from tkinter import messagebox
import easygui
from PIL import Image, ImageDraw 

def start(flag):

    def encrypt():
        flag = 1
        array_color = []
        def create_color(crypt):
            tmp = str(crypt)
            l = len(tmp)
            colors = []
            while l >= 6:
                t = tmp[l-6:]
                tmp = tmp[:l-6]
                colors.append(t)
                l -= 6
            if l == 0:
                return colors
            t = tmp
            while l < 6:
                t = "0" + t
                l += 1
            colors.append(t)
            return colors

        def print_color(colors):
            if array_color:
                for i in array_color:
                    i.place_forget()
                array_color.clear()
            white = (255, 255, 255)
            image1 = Image.new("RGB", (530, 530), white)
            draw = ImageDraw.Draw(image1)
            coord_x = 10 
            coord_y = 150
            x1, y1, x2, y2 = 0, 0, 50, 50
            count = 0
            ind = 0
            for i in range(len(colors) - 1, -1, -1):
                mycolor = '#'+ colors[i]
                temp = Label(bg = mycolor, width = 5, height = 3)
                temp.place(x = coord_x, y = coord_y)
                ind += 1
                widgets_crypte.append(temp)
                array_color.append(temp)
                draw.rectangle(((x1, y1), (x2, y2)), fill = mycolor)
                x1 += 60; x2 += 60
                coord_x += 50
                #coord_y += 50
                if (len(colors) - i) % 9 == 0:
                    count += 1
                    x1, y1, x2, y2 = 0, 60 * count, 50, 50 + (60 * count)
                if ind % 10 == 0:
                    coord_x = 10
                    coord_y += 70
            filename = "my_drawing.png"
            image1.save(filename)


        def enter_message():
            s = message.get()
            tmp = to_10(s, 36)
            res = from_10(tmp, 16)
            print_color(create_color(res))

        def exit():
            for i in widgets_crypte:
                i.place_forget()
            start(flag)

        for i in widgets_main:
            i.place_forget()
        widgets_main.clear()

        widgets_crypte = []

        label_enter = Label(text = "Введите сообщение:", justify=CENTER, font="Verdana 14", bg = 'white')
        label_enter.place(x = 45, y = 40)
        widgets_crypte.append(label_enter)
    
        message = StringVar()
        e = Entry(textvariable = message, width = 60)
        e.place(x = 45, y = 100)
        widgets_crypte.append(e)

        button_enter = Button(text = "Ввод", command = enter_message, font="Verdana 10")
        button_enter.place(x = 450, y = 98)
        widgets_crypte.append(button_enter)

        button_exit = Button(text = "Вернуться назад", command = exit)
        button_exit.place(x = 380, y = 460)
        widgets_crypte.append(button_exit)

    if flag == 0:
        root = Tk()
        root.title("Шифровальщик")
        field = Canvas(root, width=500, height=500, bg='white')
        field.pack()

    widgets_main = []

    greeting = Label(text = "Добро пожаловать в шифровальщик.\nВы хотите:", justify=CENTER, font="Verdana 14", bg = 'white')
    greeting.place(x = 60, y = 50)
    widgets_main.append(greeting)

    button_encrypt = Button(command = encrypt, text = "Зашифровать", width = 20, height = 10)
    button_encrypt.place(x = 135, y = 200)
    widgets_main.append(button_encrypt)

    button_decrypt = Button(command = decrypt, text = "Расшифровать", width = 20, height = 10)
    button_decrypt.place(x = 135, y = 300)
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

flag = 0
start(flag)
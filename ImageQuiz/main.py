from tkinter import *
from tkinter import ttk
from tkinter import Canvas
from tkinter import NW
from PIL import Image, ImageTk
import tkinter.font as tkFont


def check(event):
    if answer.get() == '北海道':
        print("正解！！")
    else:
        print("ざんねん、正解は「{}」でした！".format('北海道'))


root = Tk()
root.title('都道府県クイズアプリ')
root.geometry("640x640")

# フレームの作成
area_question = ttk.Frame(root, padding=10)
area_image = ttk.Frame(root, padding=10)
area_hints = ttk.Frame(root, padding=10)
area_button = ttk.Frame(root, padding=10)
area_text = ttk.Frame(root, padding=10)
area_answer = ttk.Frame(root, padding=10)

with open('question.txt', encoding='utf-8') as file:
    data = file.readlines()

q, im, h1, h2, h3, ans = data[0].split(',')
question = ttk.Label(area_question, font=("", 20), text="問題：" + q)
hint1 = ttk.Label(area_hints, font=("", 16), text="ヒント1: " + h1)
hint2 = ttk.Label(area_hints, font=("", 16), text="ヒント2: " + h2)
hint3 = ttk.Label(area_hints, font=("", 16), text="ヒント3: --")

# 画像表示
img = Image.open("image/" + im)
img = img.resize((400, 240))
img = ImageTk.PhotoImage(img)

# Label 1
picture = ttk.Label(area_image, image=img)

t = StringVar()
answer = ttk.Entry(area_text, font=("", 20), textvariable=t)
button1 = ttk.Button(area_answer, text='ヒントを出す')
button2 = ttk.Button(area_answer, text='答える！')
button1.bind("<Button-1>", check)
button2.bind("<Button-1>", check)


# レイアウト
area_question.pack()
question.pack()

area_image.pack()
picture.pack()

area_hints.pack()
hint1.pack()
hint2.pack()
hint3.pack()

area_text.pack()
answer.pack()

area_answer.pack()
button1.pack()
button2.pack()

# ウィンドウの表示開始
root.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import json


def getHint():
    global hints_now, img
    if hints_now == 1:
        # ヒント１をセット
        hint1_label["text"] = "ヒント1: " + data[question_number]["hint1"]
    elif hints_now == 2:
        hint2_label["text"] = "ヒント2: " + data[question_number]["hint2"]
    elif hints_now == 3:
        # 画像をセット
        img = Image.open("image/" + data[question_number]["image"])
        img = img.resize((400, 400))
        img = ImageTk.PhotoImage(img)
        picture_label.configure(image=img)
    hints_now += 1


def checkAnswer():
    input_text = textarea.get()
    textarea.delete(0, END)

    if input_text == data[question_number]["answer"]:
        textarea.insert(0, "【○正解！】")
        textarea.insert(END, "　入力した答え：" + input_text)
    else:
        textarea.insert(0, "【×ざんねん】正解は「" + data[question_number]["answer"] + "」でした！")
        textarea.insert(END, "　入力した答え：" + input_text)


def nextQuestion():
    global img, question_number, hints_now
    textarea.delete(0, END)
    hints_now = 1
    question_number += 1

    if question_number < question_max:

        # 問題文をセット
        question_label["text"] = "問題：" + data[question_number]["question"]

        # 前のヒントをリセット
        hint1_label["text"] = "ヒント1: "
        hint2_label["text"] = "ヒント2: "
        img = Image.open("hint3.jpg")
        img = ImageTk.PhotoImage(img)
        picture_label.configure(image=img)

    else:
        endQuiz()


def endQuiz():
    textarea.delete(0, END)
    textarea.insert(0, "すべてのクイズに答えました！")


# 外部データの読み込み
with open("data.json", 'r', encoding="utf-8") as file:
    data = json.load(file)

# 変数の作成
question_max = len(data)
question_number = -1
hints_now = 0


# メインウィンドウの描画
root = Tk()
root.title('都道府県クイズアプリ')
root.resizable(width=False, height=False)
root.geometry("640x640")

# ラベルの作成
question_label = ttk.Label(root, font=("", 16), padding=10, text="問題文ラベル")
hint1_label = ttk.Label(root, font=("", 12), padding=5, text="ヒント１ラベル")
hint2_label = ttk.Label(root, font=("", 12), padding=5, text="ヒント２ラベル")
img = Image.open("hint3.jpg")
img = ImageTk.PhotoImage(img)
picture_label = ttk.Label(root, padding=5, image=img)

# 答え入力欄の作成
text = StringVar()
textarea = ttk.Entry(root, font=("", 16), width=640, textvariable=text)

# ボタンの作成
button1 = ttk.Button(root, padding=5, text='ヒントを出す', command=lambda: getHint())
button2 = ttk.Button(root, padding=5, text='答える！', command=lambda: checkAnswer())
button3 = ttk.Button(root, padding=5, text='次の問題', command=lambda: nextQuestion())

# ウィジェットの配置
question_label.pack()
hint1_label.pack()
hint2_label.pack()

picture_label.pack()

textarea.pack()
button1.pack(side='left', padx=60, pady=10)
button2.pack(side='left', padx=60)
button3.pack(side='left', padx=60)

# 第一問目を表示
nextQuestion()

# ウィンドウの表示開始
root.mainloop()
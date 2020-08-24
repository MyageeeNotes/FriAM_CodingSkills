from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# 専用ライブラリ
from ImageQuiz import mondaishu


def getHint(event, data):
    print(hint1)


def setAnswer(event, mondai):
    input = textarea.get()
    textarea.delete(0, END)

    if input == mondai.data[4]:
        textarea.insert(0, "正解！！")
        textarea.insert(END, "入力した答え：" + input)
    else:
        textarea.insert(0, "ざんねん、正解は「" + mondai.data[4] + "」でした！")
        textarea.insert(END, "入力した答え：" + input)


def updateQuestion(event, mondai):
    mondai.next()
    # 問題文をセット
    question["text"] = "問題：" + mondai.data[0]
    # ヒントをセット
    hint1["text"] = "ヒント1: " + mondai.data[1]
    hint2["text"] = "ヒント1: " + mondai.data[2]
    # 画像をセット
    img = Image.open("image/" + mondai.data[3])
    img = img.resize((400, 400))
    img = ImageTk.PhotoImage(img)
    picture["image"] = img


# メインウィンドウの描画
root = Tk()
root.title('都道府県クイズアプリ')
root.resizable(width=False, height=False)
root.geometry("640x640")

# フレームの作成
question_frame = ttk.Frame(root, padding=10)
text_frame = ttk.Frame(root, padding=10)
answer_frame = ttk.Frame(root, padding=10)

with open('question.txt', encoding='utf-8') as file:
    file = file.read().splitlines()
    mondai = mondaishu.Mondaishu(file)

# ラベルの作成
question = ttk.Label(question_frame, font=("", 16), padding=10)
hint1 = ttk.Label(question_frame, font=("", 12), padding=5)
hint2 = ttk.Label(question_frame, font=("", 12), padding=5)
picture = ttk.Label(question_frame)

# 答え入力欄の作成
t = StringVar()
textarea = ttk.Entry(answer_frame, font=("", 16), width=640, textvariable=t)

# ボタンの作成
button1 = ttk.Button(answer_frame, padding=10, text='ヒントを出す')
button2 = ttk.Button(answer_frame, padding=10, text='答える！')
button3 = ttk.Button(answer_frame, padding=10, text='次の問題')
button1.bind("<Button-1>", getHint(data=mondai))
button2.bind("<Button-1>", setAnswer(data=mondai))
button3.bind("<Button-1>", updateQuestion(data=mondai))


# レイアウト
question_frame.pack()
question.pack()
hint1.pack()
hint2.pack()
picture.pack()

text_frame.pack()
textarea.pack()

answer_frame.pack()
button1.pack(pady=10, padx=60, side='left')
button2.pack(padx=60, side='left')
button3.pack(padx=60, side='left')

updateQuestion(question)

# ウィンドウの表示開始
root.mainloop()

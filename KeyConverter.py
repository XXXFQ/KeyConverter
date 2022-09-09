import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import os
import sys

class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets_tab1()
        self.create_widgets_tab2()
        self.create_widgets_about()
        self.Keycode_box2()

    #----------------------------------タブ1---------------------------------
    def create_widgets_tab1(self):
        # テキストボックス
        self.Keycode_box1 = ttk.Entry(tab[0], width = 20, justify = tk.CENTER)
        self.Keycode_box1.insert(tk.END, 'DD000000 00000000')
        self.Keycode_box1["state"] = "readonly"
        self.Keycode_box1.place(x=76, y=18)

        # チェックボックス
        self.check_value = {}
        self.chk = [0 for i in range(23)]
        keys = [0 for i in range(23)]
        for i in range(23):
            if i > 11:
                line = 1
                Column = i - 12
            else:
                line = 0
                Column = i
            keys[i] = tk.Label(tab[0], text=self.keysList(line, Column))
            self.check_value[i] = tk.BooleanVar() #True or False
            self.chk[i] = tk.Checkbutton(tab[0], variable = self.check_value[i], command = self.KeyConversion)
        #A
        self.chk[0]["text"] = "A"
        self.chk[0].place(x=240, y=155)
        #B
        self.chk[1].place(x=220, y=175)
        keys[1].place(x=225, y=194)
        #Select
        self.chk[2]["text"] = "Select"
        self.chk[2].place(x=210, y=240)
        #Start
        self.chk[3]["text"] = "Start"
        self.chk[3].place(x=210, y=220)
        #DPad→
        self.chk[4]["text"] = "D→"
        self.chk[4].place(x=60, y=205)
        #DPad←
        keys[5]["text"] = "D←"
        self.chk[5].place(x=20, y=205)
        keys[5].place(x=0, y=207)
        #DPad↑
        keys[6]["text"] = "D↑"
        self.chk[6].place(x=40, y=185)
        keys[6].place(x=40, y=170)
        #DPad↓
        keys[7]["text"] = "D↓"
        self.chk[7].place(x=40, y=225)
        keys[7].place(x=40, y=244)
        #R
        self.chk[8].place(x=212, y=18)
        keys[8].place(x=216, y=3)
        #L
        self.chk[9].place(x=40, y=18)
        keys[9].place(x=44, y=3)
        #X
        self.chk[10].place(x=220, y=135)
        keys[10].place(x=225, y=120)
        #Y
        self.chk[11].place(x=200, y=155)
        keys[11].place(x=190, y=157)
        #ZL
        self.chk[12].place(x=14, y=18)
        keys[12].place(x=15, y=3)
        #ZR
        self.chk[13].place(x=238, y=18)
        keys[13].place(x=240, y=3)
        #TouchScreen
        self.chk[14]["text"] = "Touch Screen"
        self.chk[14].place(x=90, y=170)
        #CS→
        self.chk[15]["text"] = "CS→"
        self.chk[15].place(x=210, y=80)
        #CS←
        self.chk[16].place(x=180, y=80)
        keys[16].place(x=152, y=82)
        #CS↑
        self.chk[17].place(x=195, y=60)
        keys[17].place(x=195, y=45)
        #CS↓
        self.chk[18].place(x=195, y=100)
        keys[18].place(x=195, y=119)
        #CPad→
        self.chk[19]["text"] = "C→"
        self.chk[19].place(x=60, y=110)
        #CPad←
        keys[20]["text"] = "C←"
        self.chk[20].place(x=20, y=110)
        keys[20].place(x=0, y=112)
        #CPad↑
        keys[21]["text"] = "C↑"
        self.chk[21].place(x=40, y=90)
        keys[21].place(x=40, y=75)
        #CPad↓
        keys[22]["text"] = "C↓"
        self.chk[22].place(x=40, y=130)
        keys[22].place(x=40, y=149)

        # コピーボタン
        copy_btn = tk.Button(tab[0],
            text = 'コピー',
            relief = "groove",
            activebackground = "Gainsboro",
            command = self.copy_text
        )
        copy_btn.place(x=100, y=40)

        # リセットボタン
        reset_btn = tk.Button(tab[0],
            text = 'リセット',
            relief = "groove",
            activebackground = "Gainsboro",
            command = self.reset_Keycode
        )
        reset_btn.place(x=140, y=40)
    
    # クリップボードへのコピーをする処理(タブ1)
    def copy_text(self):
        self.clipboard_clear()
        self.clipboard_append(self.Keycode_box1.get())
    
    # チェックを全て外す処理(タブ1)
    def reset_Keycode(self):
        for i in range(23):
            self.chk[i].deselect()
        self.KeyConversion()
    
    # キーリスト
    def keysList(self, line, Column):
        keysList = [
            ["A","B","Select","Start","DPad→","DPad←","DPad↑","DPad↓","R","L","X","Y"],
            ["ZL","ZR","Touch Screen","CS→","CS←","CS↑","CS↓","CPad→","CPad←","CPad↑","CPad↓"]
        ]
        return keysList[line][Column]
    
    # キーコード変換処理
    def KeyConversion(self):
        keyvalue = 0
        for i in range(23):
            if self.check_value[i].get():
                if i <= 11:
                    keyvalue += 1 << i
                elif i >= 12 and i <= 13: #keyが"ZL"か"ZR"だった場合の処理
                    keyvalue += 1 << (i + 2)
                elif i == 14: #keyが"Touch Screen"だった場合の処理
                    keyvalue += 1 << (i + 6)
                else: #keyが"Touch Screen"以上だった場合の処理
                    keyvalue += 1 << (i + 9)
        keyvalue = format(keyvalue, "X").zfill(8)
        self.Keycode_box1 = ttk.Entry(tab[0], width = 20, justify = tk.CENTER)
        self.Keycode_box1.insert(tk.END, "DD000000 " + f"{keyvalue}")
        self.Keycode_box1["state"] = "readonly"
        self.Keycode_box1.place(x=76, y=18)

    #----------------------------------タブ2---------------------------------
    def create_widgets_tab2(self):
        # 変換ボタン
        submit_btn = tk.Button(tab[1],
            text = '変　換',
            bg = "Cyan",
            relief = "groove",
            activebackground = "DarkCyan",
            fg = "DarkSlateGray",
            command = self.ReverseKeyConversion
        )
        submit_btn.place(x=90, y=40)

        # リセットボタン
        reset_btn = tk.Button(tab[1],
            text = 'リセット',
            relief = "groove",
            activebackground = "Gainsboro",
            command = self.Keycode_box2
        )
        reset_btn.place(x=145, y=40)

        # メッセージ出力
        result = ttk.Label(tab[1], text="結果")
        result.place(x=10, y=65)
        message_box = tk.Entry(tab[1], width = 45, state = "readonly")
        message_box.place(y=82, height=160)
        self.message = tk.Message(tab[1], width= 250, font=("Helvetica", 12))
        self.message.place(x=2, y=85)
    
    # テキストボックス
    def Keycode_box2(self):
        self.Keycode_box2 = ttk.Entry(tab[1],
            width = 20,
            justify = tk.CENTER,
            validate = 'all', # 検証をどのタイミングで行うか？を指定します
            validatecommand = (self.register(self.enty_validate), '%P'),
        )
        self.Keycode_box2.insert(tk.END, 'DD000000 00000000')
        self.Keycode_box2.place(x=76, y=18)
        self.message["text"] = ""

    # テキストボックス文字上限
    def enty_validate(self, prevalidation):
        if len(prevalidation) > 17:
            return False
        return True
    
    # キーコード逆変換
    def ReverseKeyConversion(self):
        self.message['text'] = ""
        key_text = self.Keycode_box2.get()
        if not key_text:
            messagebox.showerror("エラー!", "キーコードを入力して下さい。")
        else:
            key_text = key_text.replace("DD000000 " , "")
            try:
                key_text = int(key_text , 16)
            except ValueError:
                messagebox.showerror("エラー!", "無効な値です。")
            for i in range(12):
                if key_text & 1:
                    if not self.message['text']:
                        self.message['text'] += self.keysList(0, i)
                    else:
                        self.message['text'] += f"+{self.keysList(0, i)}"
                key_text >>= 1
            if key_text:
                key_text >>= 2
                for i in range(11):
                    if key_text & 1:
                        if not self.message['text']:
                            self.message['text'] += self.keysList(1, i)
                        else:
                            self.message['text'] += f"+{self.keysList(1, i)}"
                    if i == 1: #iが(ZR)だった場合の処理
                        key_text >>= 5
                    elif i == 2: #iが(Touch Screen)だった場合の処理
                        key_text >>= 4
                    else:
                        key_text >>= 1
    #----------------------------------説明---------------------------------
    def create_widgets_about(self):
        # フッター
        footer = tk.Label(text="© 2022 静")
        footer.place(x=120, y=275)
        
        # 説明
        texts = "用語説明:\n・DPad = 十字キー\n・CPad = スライドパッド\n・CS = Cスティック\n"
        texts += "\nキーコード変換ツール V1.0.1\n静<Twitter:@jitsuzo>"
        about = tk.Label(tab[2], text=texts, justify="left", font=("MSゴシック", "12", "bold"))
        about.place(x=0, y=5)

#アイコンパス設定
def temp_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Key Converter v1.0.1')
    root.geometry('300x310')
    root.resizable(width=False, height=False)

    #アイコン設定
    logo = temp_path('KeyConverter.ico')
    root.iconbitmap(default=logo)

    #タブ設定
    nb = ttk.Notebook(width=200, height=200)
    tab = [tk.Frame(nb) for i in range(3)]
    nb.add(tab[0] , text="変換")
    nb.add(tab[1] , text="逆変換")
    nb.add(tab[2] , text="説明")
    nb.pack(expand=True, fill='both', padx=10, pady=10)

    app = Application(root)
    app.mainloop()
import time
import threading
import tkinter as tk

# e = 元件(父親元件)
# e.排版()  pack(上下左右) grid(表格) absolute(絕對)

# main thread(UI thread): 主執行緒
# 耗時的工作絕對不能在主執行緒做

class MyFrame(tk.LabelFrame):

    def __init__(self, root):
        tk.LabelFrame.__init__(self, root, text="bmi計算機")
        # 標籤: Label
        self.l1 = tk.Label(self, text="輸入身高:")
        self.l1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 單行輸入: Entry
        self.e1 = tk.Entry(self)
        self.e1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 標籤: Label
        self.l2 = tk.Label(self, text="輸入體重:")
        self.l2.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 單行輸入: Entry
        self.e2 = tk.Entry(self)
        self.e2.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 按紐: Button
        self.b1 = tk.Button(self, text="計算", command=self.bmi)
        # tk.X
        self.b1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        self.result = tk.Label(self, text="按上面按鈕計算...")
        self.result.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)

    def bmi(self):
        def work():
            self.b1["state"] = tk.DISABLED
            self.result["text"] = "計算中..."
            time.sleep(5)
            h = float(self.e1.get())
            w = float(self.e2.get())
            ans = w / (h / 100) ** 2
            # 第二時間
            self.result["text"] = str(ans)
            self.b1["state"] = tk.ACTIVE
        #
        t1 = threading.Thread(target=work)
        t1.start()

window = tk.Tk()
window.geometry("500x500+100+100")
f1 = MyFrame(window)
f1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20)
f2 = MyFrame(window)
f2.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20)
window.mainloop()





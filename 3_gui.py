import tkinter as tk

# e = 元件(父親元件)
# e.排版()  pack(上下左右) grid(表格) absolute(絕對)

window = tk.Tk()
window.geometry("500x500+100+100")
# 先創Frame
f1 = tk.Frame(window)
f1.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
# 標籤: Label
l1 = tk.Label(f1, text="輸入身高:")
l1.pack(expand=True, fill=tk.BOTH, pady=10)
# 單行輸入: Entry
e1 = tk.Entry(f1)
e1.pack(expand=True, fill=tk.BOTH, pady=10)
# 標籤: Label
l2 = tk.Label(f1, text="輸入體重:")
l2.pack(expand=True, fill=tk.BOTH, pady=10)
# 單行輸入: Entry
e2 = tk.Entry(f1)
e2.pack(expand=True, fill=tk.BOTH, pady=10)
# 按紐: Button
b1 = tk.Button(f1, text="計算")
# tk.X
b1.pack(expand=True, fill=tk.BOTH, pady=10)
result = tk.Label(f1, text="按上面按鈕計算...")
result.pack(expand=True, fill=tk.BOTH, pady=10)
window.mainloop()
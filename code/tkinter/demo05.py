import tkinter as tk

windows = tk.Tk()
windows.title('Listbox')
windows.geometry('200x200')

# 创建一个标签
var1 = tk.StringVar()
l = tk.Label(
    windows,
    textvariable = var1,
    bg = 'yellow',
    width = 15,
    height = 2
)
l.pack()

def print_select():
    value = lb.get(lb.curselection())   # 获取当前选中的文本
    var1.set(value)

b1 = tk.Button(
    windows,
    text = 'print selection',
    width = 15,
    height = 2,
    command = print_select,
)
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44)) # 为变量设置值

lb = tk.Listbox(
    windows,
    listvariable = var2,    # 将var2的值赋给Listbox
)



# 创建一个list并将值添加到Listbox
list_item = [1,2,3,4]
for item in list_item:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(2,'second')
lb.pack()

windows.mainloop()
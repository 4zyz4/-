from tkinter import Label, Button, messagebox, Frame
from tkinterdnd2 import *
from PIL import Image
import os

def replace_colors(image_path):
    # 打开图像
    image = Image.open(image_path)
    # 将图像转换为RGB模式
    image = image.convert('RGB')
    # 获取图像的像素数据
    pixels = list(image.getdata())
    # 创建一个新的像素列表
    new_pixels = []

    # 遍历每个像素
    for pixel in pixels:
        # 如果像素颜色为灰色，则将其改为白色
        if pixel[0] >= 188 and pixel[1] >= 188 and pixel[2] >= 188:
            new_pixels.append((255, 255, 255))
        else:
            new_pixels.append(pixel)
    
    # 创建一个新的图像
    new_image = Image.new('RGB', image.size)
    new_image.putdata(new_pixels)
    # 保存新的图像
    new_image.save('out.jpg')
    os.system("move out.jpg C:/Users/%Username%/Desktop")
    return 

def drop(event):
    global file_path
    file_path = event.data
    label.config(text="文件已拖入:"+file_path)

def convert_image():
    if file_path:
        replace_colors(file_path)
        messagebox.showinfo("完成","转换完成,已在桌面保存为out.jpg")
        label.config(text="拖入一张图片")

# 创建主窗口
root = TkinterDnD.Tk()
root.title("去除水印")
root.geometry("600x300")

# 创建并放置标签和按钮

frame = Frame(root, bd=1, relief="solid")
frame.pack(pady=40, padx=20)

label = Label(frame, text="在此处拖入一张图片",font=("Microsoft YaHei", 16))
label.pack(pady=20)

button = Button(root, text="转换", command=convert_image,font=("Microsoft YaHei", 20))
button.pack(pady=10)

# 绑定拖放事件
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# 运行主循环
root.mainloop()

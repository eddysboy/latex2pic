# 23秋 计算机程序设计C2大作业
#Author 刘彦宏 娄彦轩

import json
import keyboard
import pystray
from plyer import notification
import threading
import os
import tkinter as tk
import threading
# from transfer import ransfer
# from transfer import *
import transfer
from compute import compute
from PIL import Image

hotkey_transfer=''
hotkey_compute=''
exit_code=''
border_width = 20
ICON_PATH = 'icon.ico'

def on_click(icon, item):
    icon.stop()
    os._exit(0)

def config_all_hotkey():
    keyboard.add_hotkey(hotkey_transfer,transfer.transfer)
    keyboard.add_hotkey(hotkey_compute,compute)
    print('Config Success!')



root=tk.Tk()
root.geometry('300x200')
root.title('Configuration Menu')
root.iconbitmap(ICON_PATH)
root.protocol('WM_DELETE_WINDOW',root.withdraw)
msg1 = tk.Label(root,text='Transfer Hotkey:')
entry1 = tk.Entry(root)
msg2 = tk.Label(root,text='Compute Hotkey:')
entry2 = tk.Entry(root)
msg3 = tk.Label(root,text='Exit Hotkey:')
entry3 = tk.Entry(root)
msg4 = tk.Label(root,text='Border Width (px):')
entry4 = tk.Entry(root)
msg1.grid(row=0,column=0,padx=5,pady=5)
entry1.grid(row=0,column=1,padx=5,pady=5)
msg2.grid(row=1,column=0,padx=5,pady=5)
entry2.grid(row=1,column=1,padx=5,pady=5)
msg3.grid(row=2,column=0,padx=5,pady=5)
entry3.grid(row=2,column=1,padx=5,pady=5)
msg4.grid(row=3,column=0,padx=5,pady=5)
entry4.grid(row=3,column=1,padx=5,pady=5)
def save_f():
    global hotkey_transfer,hotkey_compute,exit_code,border_width
    hotkey_transfer=entry1.get()
    hotkey_compute=entry2.get()
    exit_code=entry3.get()
    border_width = entry4.get()
    settings={'Transfer':hotkey_transfer,'Compute':hotkey_compute,'exit_code':exit_code,'border_width':border_width}
    f=open("./settings.json","w")
    f.write(json.dumps(settings))
    f.close()
    keyboard.clear_all_hotkeys()
    config_all_hotkey()
    root.withdraw()

def config_reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)
    entry1.insert(0, 'alt+ctrl+shift+t')
    entry2.insert(0, 'alt+ctrl+shift+c')
    entry3.insert(0, 'alt+ctrl+shift+esc')
    entry4.insert(0, 10)

btn1 = tk.Button(root, text = 'Save', command = save_f)
btn2 = tk.Button(root, text = 'Cancel', command = root.withdraw)
btn3 = tk.Button(root, text = 'Reset', command = config_reset)
btn1.grid(row=4,column=0,columnspan=3,sticky='w')
btn2.grid(row=4,column=0,columnspan=3)
btn3.grid(row=4,column=0,columnspan=3,sticky='e')
# btn1.pack()
# btn2.pack()
# btn3.pack()
root.withdraw()
# root.mainloop()
# def open_configuration_menu():
#     root.deiconify()


if __name__=='__main__':

    try:
        f=open("./settings.json","r")
        settings=json.loads(f.read())
        hotkey_transfer=settings['Transfer']
        hotkey_compute=settings['Compute']
        exit_code=settings['exit_code']
        border_width = settings['border_width']
        entry1.insert(0, hotkey_transfer)
        entry2.insert(0, hotkey_compute)
        entry3.insert(0,exit_code)
        entry4.insert(0,border_width)
        print("读取到配置文件并加载完成.")
        notification.notify(
            title = "启动成功",
            message = "读取到配置文件并加载完成。",
            timeout = 1,
            app_icon = "icon.ico"
        )
    except:
        config_reset()
        root.deiconify()
        # s=input("未检测到配置文件.(或者配置文件错误)是否需要创建默认配置文件?(y/N)")
        # while s!='y' and s!='N':
        #     s=input("非法输入, 请输入y或N:")
        # if s=='N':
        #     exit(0)
        # f=open("./settings.json","w")
        # default_settings={'Transfer':'alt+ctrl+t','Compute':'alt+ctrl+c','exit_code': 'alt+ctrl+esc'}
        # f.write(json.dumps(default_settings))
        # print("成功创建配置文件. 请按需修改配置文件后重新启动程序.")  
        exit(0)
    finally:
        if f:
            f.close()
# add a small icon to the system tray
    icon_image = Image.open(ICON_PATH)
    menu = {
        pystray.MenuItem('配置', root.deiconify),
        pystray.MenuItem('退出', on_click),
    }
    icon = pystray.Icon("latex2pic", icon_image, "latex2pic", menu)
    runicon = threading.Thread(target = icon.run)
    runicon.start()
# end of icon
    print(hotkey_transfer)
    try:
        config_all_hotkey()
    except:
        print('Configuration setting error.')
    print("Running...")
    root.mainloop()
    # keyboard.wait(exit_code)
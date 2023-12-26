import win32con
import win32clipboard
import win32gui
import time
import keyboard
import pyperclip

def get_selected_text():

    # win32clipboard.OpenClipboard()
    # original=win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    # win32clipboard.CloseClipboard()
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.5)
    selected_text=pyperclip.paste()
    # win32clipboard.OpenClipboard()
    # selected_text=win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    # win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT,original)
    # win32clipboard.CloseClipboard()

    return selected_text

# def get_selected_text():
#     hwnd=win32gui.GetForegroundWindow()

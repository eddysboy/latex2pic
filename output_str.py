import win32con
import win32clipboard
import time
import keyboard
import pyperclip

def output_str(strr):

    # win32clipboard.OpenClipboard()
    # original=win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
    # #win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT,strr)
    # win32clipboard.CloseClipboard()

    pyperclip.copy(strr)
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+v')

    # win32clipboard.OpenClipboard()
    # win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT,original)
    # win32clipboard.CloseClipboard()

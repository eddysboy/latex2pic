# import sys
import get_selected_text
import win32clipboard
import time
import keyboard
from io import BytesIO
import win32con
# sys.path.append('D:\document\Code\homework\C2\latex2pic\ch')
from latex_trans import *
def transfer():
	str = get_selected_text.get_selected_text()
	pic = latex_to_image_bytes(str)

	output=BytesIO()
	pic.save(output,'BMP')
	data=output.getvalue()[14:]
	output.close()

	# print(data)

	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(win32con.CF_DIB,data)
	win32clipboard.CloseClipboard()
	time.sleep(0.5)

	keyboard.press_and_release('ctrl+v')

	print("sucess")
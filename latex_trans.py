
from pprint import pprint
import os
import imgkit
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.binary_location = os.getcwd() + '/application'
browser = webdriver.Chrome(options = chrome_options)
# browser = webdriver.Chrome(exec = , options = chrome_options)
browser.set_window_size(1920, 1080)
border_width = 1
def latex_to_html(latex_file, html_file): # convert latex to html
	print(os.getcwd())
	os.system(os.getcwd() + "/Pandoc/pandoc.exe " + latex_file + " -s --katex -o " + html_file) # use pandoc to convert latex to html

def html_to_image_file(html_file, image_file): # convert html to image
	path = os.getcwd() + '/' + html_file # get the path of the html file
	browser.get('file:///' + path) # open the html file
	browser.fullscreen_window() # maximize the window
	browser.save_screenshot(os.getcwd() + '/' + image_file) # save the screenshot
	print('finished') # debug

def html_to_image_bytes(html_file) -> bytes: # convert html to image(bytes)
	path = os.getcwd()+'/'+html_file # get the path of the html file
	browser.get('file:///'+path) # open the html file
	browser.fullscreen_window() # maximize the window
	return browser.get_screenshot_as_png() # get the screenshot

def latex_to_image_bytes(str):
	tex_file = open('temp/text.tex', mode = 'wb') # open the tex file
	full_tex = '\\begin{document}\n$$\n' + str +'\n$$\n\\end{document}\n' # get the full tex
	# full_tex.encode('byte')
	tex_file.write(full_tex.encode("UTF-8")) # write the full tex to the tex file
	tex_file.close() # close the tex file
	latex_to_html('temp/text.tex', 'temp/index.html') # convert the tex file to html file
	html_to_image_file('temp/index.html','temp/output.png') # convert the html file to image file
	img=Image.open('temp/output.png') # open the image file
	# img = Image.open(html_to_image_bytes('temp/index.html'))
	width, height = img.size # get the size of the image
	min_width = 114514 # init
	max_width = 0
	min_height = 114514
	max_height = 0
	for y in range(height): 
		for x in range(width): 
			(r, g, b, a)=img.getpixel((x,y)) # get the pixel value
			if(r < 250 or g < 250 or b < 250): # if the pixel is not white
				min_width = min(min_width, x) # update the min_width
				min_height = min(min_height, y) # update the min_height
				max_width = max(max_width, x) # update the max_width
				max_height = max(max_height, y) # update the max_height

	min_width = max(0, min_width - border_width) # make sure the min_width is not negative
	min_height = max(0, min_height - border_width) # make sure the min_height is not negative
	max_width = min(width, max_width + border_width) # make sure the max_width is not larger than the width
	max_height = min(height, max_height + border_width) # make sure the max_height is not larger than the height
	if(min_width <= max_width and min_height <= max_height):
		img = img.crop((min_width, min_height, max_width, max_height)) # crop the image
	return img

def set_border_width(x):
	border_width = x

# DEBUG

# while 1:
# 	# print("start\n")
# 	str = input()
# 	img = latex_to_image_bytes(str)
# 	img_file=open('temp/img.png',mode='wb')
# 	img_file.write(img)
# 	img_file.close()

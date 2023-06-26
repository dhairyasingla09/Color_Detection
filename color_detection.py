#this code belongs to dhairya singla

# pip install pandas opencv-python

import cv2
import pandas as pd
import os
import matplotlib
import sklearn

img_path = 'new1.jpg'
csv_path = 'ColorList.csv'

# reading csv file from the folder
col_headers = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=col_headers, header=None)

# reading image from the folder
img = cv2.imread(img_path)
img = cv2.resize(img, (800,600))

#declaring global variables 
clicked = False
r = g = b = xpos = ypos = 0

#function to calculate minimum distance from all colors and get the almost same colour

def get_color_name(R,G,B):
	minimum = 1000
	for i in range(len(df)):
		d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
		if d <= minimum:
			minimum = d
			cname = df.loc[i, 'color_name']

	return cname

#function to get x,y coordinates of the mouse click
def draw_function(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x
		ypos = y
		b,g,r = img[y,x]
		b = int(b)
		g = int(g)
		r = int(r)


# creating new window
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
	cv2.imshow('image', img)
	if clicked:
		#cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 will fill the entire rectangle
		cv2.rectangle(img, (20,20), (600,60), (b,g,r), -1)

		#Creating alphabetical string to display color name and RGB values
		text = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

		#cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
		cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)

		#For light colours like white or pink we will display text in black colour as it will be visible
		if r+g+b >=600:
			cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break


#destroys all windows
cv2.destroyAllWindows()


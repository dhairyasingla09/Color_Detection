## Prerequisites
Before starting with this Python project with source code, we need to know about some of the computer vision libraries of Python, such as OpenCV and Pandas.
OpenCV, Pandas, and Numpy are the Python packages that are necessary for this project. 

### About the Python Project
In this color detection Python project, I am going to build an application through which we can automatically get the name of the color by clicking on them. So for this, we will have a data file that contains the color name and its values. Then we will calculate the distance from each color and find the shortest one.<br>

#### The project folder contains 3 files:<br>
1) Color_detection.py – main source code of our project.<br>
2) Colorpic.jpg – sample image for experimenting.<br>
3) Colors.csv – a file that contains our dataset.<br>


The pandas library is very useful when we need to perform various operations on data files like CSV. pd.read_csv() reads the CSV file and loads it into the pandas DataFrame. We have assigned each column with a name for easy accessing.<br>

First, we created a window in which the input image will display. Then, we set a callback function which will be called when a mouse event happens.
With these lines, we named our window as ‘image’ and set a callback function which will call the draw_function() whenever a mouse event occurs.<br>

draw_function will calculate the rgb values of the pixel which we double click. The function parameters have the event name, (x,y) coordinates of the mouse position, etc.

We have the r,g and b values. Now, we need another function which will return us the color name from RGB values. Our distance is calculated by this formula:
d = abs(Red – ithRedColor) + (Green – ithGreenColor) + (Blue – ithBlueColor).


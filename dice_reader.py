### Functions that allow the dice to be read from the webcam and validate that we have the correct number of dice

# Data related imports
from multiprocessing.connection import wait
from cv2 import imshow, waitKey
from matplotlib.pyplot import axes
import numpy as np
import matplotlib.axes
from numpy.linalg import norm 
import cv2

def read_dice():
  cap = cv2.VideoCapture(0)


  #reads frame
  ret, frame = cap.read()
  #grayscales image, blurs it, finds threshold img, edge dectetion algorithm, and finds all contours
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  blur= cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)
  ret, thresh = cv2.threshold(blur,170, 255,cv2.THRESH_BINARY)
  edge = cv2.Canny(thresh, 50, 230)
  contours =  cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
  #sorts contours to size that will isolate dice
  diceRects = []
  for c in contours:
    process = False
    rect = cv2.minAreaRect(c)
    center = rect[0]
    width = rect[1][0]
    height = rect[1][1]
    if width*height > 3000 and width*height < 4500:
      process = True
    if process:
      diceRects.append(rect)
  diceRects = diceRects[::2]
  diceCounts = []
  # Breaks down dice contours into separate images
  for i in diceRects:
    rect = i
    angle = rect[2]
    width = round(rect[1][0])
    height = round(rect[1][1])
    rotate_matrix = cv2.getRotationMatrix2D(rect[0], rect[2], 1.0)
    rotated = cv2.warpAffine(src=gray, M=rotate_matrix, dsize=(gray.shape[1::-1]), flags = 2)
    cropped = cv2.getRectSubPix(rotated, patchSize = (width, height), center = rect[0])
    ret, thresh = cv2.threshold(cropped,170, 255,cv2.THRESH_BINARY)
    # Finds contours on each die, sizes them to only isolate the dots, and then counts them to find the dice number
    contours = cv2.findContours(thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
    dotRects = []
    for c in contours:
      rect = cv2.minAreaRect(c)
      center = rect[0]
      width = rect[1][0]
      height = rect[1][1]
      process = False
      if width*height > 75 and width*height < 350:
        process = True
      if process:
        dotRects.append(rect)
    if len(dotRects) >= 1 and  len(dotRects) <= 6:
      diceCounts.append(len(dotRects)) 
  return(diceCounts)

def validate_dice():
    dice_counts = read_dice()
    if len(dice_counts) != 5:
        print("These are the dice we found: ", end = ' ')
        print(", ".join(map(str, dice_counts)))
        print("")
        if len(dice_counts) < 5:
          print("It appears we are missing one or more dice.")
          for i in range (5 - len(dice_counts)):
            missing = int(input("Please enter one of the missing dice values: ")) 
            dice_counts.append(missing) 
        else:
          print("It appears we are getting extra dice.")
          for i in range (len(dice_counts) - 5):
            extra = int(input("Please enter one of the extra dice values: ")) 
            dice_counts.remove(extra)
    return dice_counts

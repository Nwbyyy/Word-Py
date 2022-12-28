from PIL import Image, ImageGrab, ImageFilter #To take a screenshot to get question
import pytesseract #To interpret text on screen
import csv #To import csv dictionary
import pyautogui #To type in the answer
import pydirectinput #To submit the answer
from pynput import keyboard #To detect keypress
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #To locat pytesseract

import time




#binarization function
def binarize(img):

  #initialize threshold
  thresh=31

  #convert image to greyscale
  img=img.convert('L') 

  width,height=img.size

  #traverse through pixels 
  for x in range(width):
    for y in range(height):

      #if intensity less than threshold, assign white
      if img.getpixel((x,y)) < thresh:
        img.putpixel((x,y),0)

      #if intensity greater than threshold, assign black 
      else:
        img.putpixel((x,y),255)

  return img



#Returns a list of words imported from the text file
def import_words():
    #Creates list of many English words
    return open("words.txt", "r").read().split("\n")

#Returns the string containing the part of the word that is needed to solve
def get_letters():
    top_img = ImageGrab.grab(bbox=(747,382,897,419))
    bot_img = ImageGrab.grab(bbox=(746,657,882,698))
    top_img = top_img.convert("L")
    bot_img = bot_img.convert("L")
    top_cleaned = binarize(top_img)
    bot_cleaned = binarize(bot_img)
    top_cleaned = top_cleaned.resize({1800,444})
    bot_cleaned = bot_cleaned.resize({1832,492})
    top_cleaned.show()

    letters_top = pytesseract.image_to_string(top_img)
    letters_bottom = pytesseract.image_to_string(bot_img)
    
    if len(letters_top) > 0 and len(letters_bottom) == 0:
        return letters_top
    elif len(letters_bottom) > 0 and len(letters_top) == 0:
        return letters_bottom
    elif len(letters_top) > 0 and len(letters_bottom) > 0:
        answer = input("The top and bottom contains letters which would you like to use? (t/b)\nTop letters: " + letters_top + "\nBottom letters: " + letters_bottom)
        if answer == "t":
            return letters_top
        elif answer == "b":
            return letters_bottom
    elif len(letters_top) == 0 and len(letters_bottom) == 0:
        print("There are no letters deteceted here.")
        
        
list = import_words()
letters = get_letters().lower()
letters = letters[0:len(letters) - 1]
print(letters)
for i in list:
    if letters in i:
        print(i)
        break

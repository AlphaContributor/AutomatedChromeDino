import pyautogui                   #import python auto graphical user interface library
from PIL import Image, ImageGrab   #Import Image and Image Grab from Python Imaging library
#from numpy import asarray
import time

def hit(key):              #function for using down key
    pyautogui.keyDown(key)  
    return

def isCollide(data):       #To check a rectangular area for birds
 
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")         #Hit down if birds are present
                return

    for i in range(300, 415):     #To check a rectangular area for Cacti
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")              #Hit up to jump when cacti are present
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  #Loop to process images and find information about cacti and birds
        data = image.load()
        isCollide(data)
            
       
        '''
     
        for i in range(275, 325):
            for j in range(563, 650):
                data[i, j] = 0
        
       
        for i in range(250, 300):
            for j in range(410, 563):
                data[i, j] = 171

        image.show()
        break
      '''


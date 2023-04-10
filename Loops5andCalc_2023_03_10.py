# File:     Loop5andCalc_2023_03_10
# Version:  0.0.01
# Author:   Susan Haynes
# Comments/Notes: 
#   (0,0) coordinates are the top left corner of the screen for 1920x1080
#   (0,0) coordinates are the bottom right corner of the screen for 1919x1079
# Online References: 
#   https://pypi.org/project/PyAutoGUI/
#   https://pyautogui.readthedocs.io/en/latest/mouse.html
# Revision History: N/A 
# To find the location on a screen open IDLE 
# >>> import pyautogui      <- this allows us to use pyautogui prompts
# >>> pyautogui.size()    <- this returns the size of the monitor
# >>> pyautogui.position()  <- this returns the exact location of where the mouse pointer is

from lib2to3.pgen2.token import ENDMARKER
import pyautogui
import subprocess                                                       # Needed to open an executable
import cv2                                                              # Needed for finding images on the screen
import time                                                             # Needed to call time to count/pause
import psutil,os                                                        # Needed for closing an executable
from PIL import Image                                                   # For opening images for testing, pillow package.
from python_imagesearch.imagesearch import imagesearch                  # For opening images for testing, pip package.
#from asyncore import read                                              # Import the library read, used for doing more than one task at a time
#from tkinter import *                                                  # Import the library tkinter, used for checking which button was pressed on the gui

# Find screen size and write values to script
screenWidth, screenHeight = pyautogui.size()                            # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position()                     # Returns two integers, the x and y of the mouse cursor's current position.

# Test of message boxes
pyautogui.alert("""Operator needs to manually adjust the focal value, dispersion
compensation B, dispersion compensation C, and contrast bar until the image is in focus. 

Press OK to continue running the scripts after adjustments have been completed.

WARNING: You will not have the option to go back after pressing OK.""")

#**************************************    LUMEDICA OQ PATHSCOPE    ***************************************************
# Open image of Main screen to find buttons from images in project folder.
imgOQ = Image.open(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\MainScreen.png")   # For testing only.
imgOQ.show()

i = 0
for i in range(0,5):
# Take a screenshot to scan and compare pictures with the screenshot for mismatched size buttons.
    im1OQ = pyautogui.screenshot()
    im1OQ.save('my_screenshotOQ.png')
    im2OQ = pyautogui.screenshot('my_screenshotOQ2.png')

    # Look for a matching image on the screen from a screenshot saved in project folder, then click on it.
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\StartScan.png"))
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\SaveB-ScanIm.png"))
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\SaveRawB.png"))
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\Main.png"))     
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\Review.png"))      
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\Configuration.png"))             
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\Advanced.png"))             
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\FolderName.png"))            
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\SampleName.png"))             

    # Click on the scroll bar and move from 0.15 to 0.40
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\Scroll.png")) 
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\onefive.png")) 
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\zerofour.png"))  
    i += 1
    print(i)
    if i == 5:
        break    

#**************************************    THORLABS KINESES GUI    ***************************************************
# Open image of Main screen to find buttons from images in project folder.
imgTL = Image.open(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\ThorLabsKinesisGui.png")   # For testing only.
imgTL.show()

j = 0
for j in range(0,5):
# Take a screenshot to scan and compare pictures with the screenshot for mismatched size buttons.
    im1TL = pyautogui.screenshot()
    im1TL.save('my_screenshotTL.png')
    im2TL = pyautogui.screenshot('my_screenshot2TL.png')

# Look for a matching image on the screen from a screenshot saved in project folder, then click on it.
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\JogUp.png"))
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\JogDn.png"))
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\TLvalue.png"))
    pyautogui.click(pyautogui.locateCenterOnScreen(r"\\RXS-FS-02\userdocs\shaynes\My Documents\R&D - Software\Python\LoopandScreenCalc_2023-03-09\Move.png"))
    j += 1
    print(j)
    if j == 5:
        break

# Open the calculator, and pause for 2 seconds before executing, this gives the calculator time to open.
subprocess.Popen('C:\\Windows\\System32\\calc.exe')                     # Open windows calculator
time.sleep(2)                                                           # wait 2 seconds to give the calc time to open, 1 second is not enough

# Declare starting position and positions to move to
y = 985                                                                 # y starting location
y_p = 50                                                                # y position to down row on the calculator
while y < 1100 :                                                        # loop until x reaches a value of 1559 (3rd column position on calculator)      

    x = 1395                                                            # x starting location
    x_p = 60                                                            # x position to move over 1 column on the calculator
    while x < 1560:                                                     # loop until y reaches a value of 1099 (3rd row position on calculator)

        pyautogui.moveTo(x, y, duration=0.1, tween=pyautogui.easeInOutQuad) # Use tweening/easing function to move mouse over 1 second.
        pyautogui.click()

        if x < 1560 and y < 1100 :                                     # if x is in the bottom row and y is in the 3rd column, go to the else statement
            pyautogui.moveTo(1605, 1085, duration=0.1, tween=pyautogui.easeInOutQuad) # +
            pyautogui.click()  
            print("X-Position initial: ", x)            
            x += x_p           
            print("X-Position end of loop: ", x)       
        
    print("Y-Position initial: ", y)
    y += y_p
    print("Y-Position end of loop: ", y)  

time.sleep(5)                                                           # wait 5 seconds to view the results
os.system("TaskKill /F /IM CalculatorApp.exe")                          # Close windows calculator
exit()


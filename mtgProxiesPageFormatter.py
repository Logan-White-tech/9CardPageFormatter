#mtgProxiesPageFormatter.py

#7-10-2022
#Logan White
#This takes playing card images and outputs printer paper sized templates with up to 9 card images for fast formatting

#When started, the code opens a dialog to choose the folder that contains the card images
#It saves the templates to the parent directory

from tkinter.tix import DirSelectBox
from PIL import Image
from tkinter.filedialog import askopenfile, askdirectory
import os
from pyparsing import nums

    #printer resolution
    #300 pixels per in 

    #printer paper size
    #8.5in x 11 in 

    #pixels per page
    #2550 x 3300
xPixels = 2550
yPixels = 3300
xPixelOffset = 30
yPixelOffset = 30

print("Select the folder that contains all of the images ")

    #choose the directory that holds the cards
folder = askdirectory(title="Choose directory with the cards", initialdir= os.getcwd())

    #error prevention
if(len(folder) == 0):
    print("No Card Folder Chosen")
    exit()

print("Select the folder that you want to store the templates")

    #choose the directory that holds the cards
templateFolder = askdirectory(title="Choose directory to save the templates", initialdir= os.getcwd())

    #error prevention
if(len(templateFolder) == 0):
    print("No Template Folder Chosen")
    exit()


directory = folder
#templateDirectory = folder[0:folder.rfind("/")] 
templateDirectory = templateFolder
    #this gets the parent folder of the card images to save the templates to

#print(directory)
#print("\n\n"+ folder+ "\n\n")


    #create object to store the full page with cards
template = Image.new(mode="RGBA", size = [xPixels,yPixels])

    #find each image in the chosen directory
os.chdir(directory)
imageFiles = []
for x in os.listdir():
    if(".png" in x or ".jpg" in x or ".jpeg" in x or ".gif" in x):
        imageFiles.append(x)
        
    #start formatting cards onto a printer paper sized canvas
numCards = 0
numSheets = 0
for card in imageFiles:
    temp = Image.open(card)
    temp.resize((745,1040))
    TLpixel = (int(numCards%3 * 1/3 * xPixels) + xPixelOffset,  int(int(numCards/3) * 1/3 * yPixels) +yPixelOffset)
    template.paste(temp, TLpixel)
    numCards = numCards+1
        #if a sheet is full(has nine cards) save it and reset the template
    if(numCards > 8):
        print("Formatted sheet " + str(numSheets))
        numCards = 0
        #template.show()
        templateName = templateDirectory + "/ProxyTemplate" + str(numSheets) + ".png"
        template.save(templateName)
        numSheets = numSheets + 1
        template = Image.new(mode="RGBA", size = [xPixels,yPixels])
    
    #case if the last template has cards save it
if(numCards > 0):
    #template.show()
    print("Formatted sheet " + str(numSheets))
    templateName = templateDirectory + "/ProxyTemplate" + str(numSheets) + ".png"
    template.save(templateName) 
#template.show()
#template.save(directory +"/ProxyTemplate.png") 

    
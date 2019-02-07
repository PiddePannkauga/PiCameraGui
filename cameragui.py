from Tkinter import *
from picamera import PiCamera

redAWB = 1.44
blueAWB = 0.88
AWBsliderRes = 0.01
sharpsliderRes = 1
gains = (redAWB,blueAWB)
camera = PiCamera() 
camera.awb_mode = 'off'
camera.awb_gains = gains
#camera.exposure_mode = 'off'
camera.vflip = True
camera.hflip = True
#camera.shutter_speed = camera.exposure_speed
#camera.drc_strength = "high"


def setRed(red):
    global redAWB 
    redAWB = float(red)
    
    gains = (redAWB,blueAWB)
    print(gains)
    camera.awb_gains = gains

def setBlue(blue):     
    global blueAWB 
    blueAWB = float(blue)
    gains = (redAWB,blueAWB)
    print(gains)
    camera.awb_gains = gains
   
def takePicture():
    camera.capture("testAWB.jpg")

def takeYuvPicture():
    camera.capture("testAWB.data", "yuv")

def setSharpness(val):
    camera.sharpness=int(val)
    #camera.digital_gain = float(val) 

def setISO(val):
    camera.iso = int(val)

def repos(val):
    previewX = master.winfo_x()
    previewY = master.winfo_y()    
    camera.start_preview(fullscreen=False,resolution=(1920,1080),window=(previewX+75,previewY+250,800,600))    


master = Tk()

previewX = master.winfo_x()
previewY = master.winfo_y()

camera.start_preview(fullscreen=False,window=(previewX+75,previewY+250,800,600))
redSlider = Scale(master,label="RedAWB",resolution=AWBsliderRes,orient=HORIZONTAL, from_=0.0, to=5.0, command=setRed)
redSlider.pack()

blueSlider = Scale(master,label="BlueAWB",resolution=AWBsliderRes,orient=HORIZONTAL, from_=0.0, to=5.0, command=setBlue)
blueSlider.pack()

isoSlider = Scale(master,label="ISO",orient=HORIZONTAL,from_=0, to=800, command = setISO)
isoSlider.pack()

sharpnessSlider = Scale(master,label="Sharpness", orient=HORIZONTAL,resolution=sharpsliderRes, from_=-100, to=100, command=setSharpness)
sharpnessSlider.pack()

frame = Frame (master,height=600, width=860)
frame.pack()

btn = Button(master, text="Take Picture", command = takePicture)
btn.pack()

btnYuv = Button(master, text="Take YUV Picture", command = takeYuvPicture)
btnYuv.pack()

master.bind("<Configure>", repos)
mainloop()

from Tkinter import *
from picamera import PiCamera

redAWB = 0.29
blueAWB = 4.43
AWBsliderRes = 0.01
brightnessSliderRes = 1
gains = (redAWB,blueAWB)
camera = PiCamera() 
camera.awb_mode = 'off'
camera.awb_gains = gains
#camera.exposure_mode = 'off'
camera.vflip = True
camera.hflip = True
camera.resolution = (800, 600)
camera.framerate = 15
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
    camera.capture("testAWB.jpg", )

def takeYuvPicture():
    camera.capture("testAWB.data", "yuv")

def setBrightness(val):
    camera.brightness=int(val)
    #camera.digital_gain = float(val) 

def setISO(val):
    camera.iso = int(val)

def setContrast(val):
    camera.contrast = int(val)


def repos(val):
    previewX = master.winfo_x()
    previewY = master.winfo_y()    
    camera.start_preview(fullscreen=False,resolution=(800,600),window=(previewX+75,previewY+350,800,600))    

def exposure():
        camera.exposure_mode=exposureMode.get().lower()

def drc():
        camera.drc_strength=drcMode.get().lower()

def mode(val):
        #flicker()
        exposure()
        drc()

master = Tk()

previewX = master.winfo_x()
previewY = master.winfo_y()

camera.start_preview(fullscreen=False,window=(previewX+75,previewY+350,800,600))
redSlider = Scale(master,label="RedAWB",resolution=AWBsliderRes,orient=HORIZONTAL, from_=0.0, to=5.0, command=setRed)
redSlider.pack()

blueSlider = Scale(master,label="BlueAWB",resolution=AWBsliderRes,orient=HORIZONTAL, from_=0.0, to=5.0, command=setBlue)
blueSlider.pack()

isoSlider = Scale(master,label="ISO",orient=HORIZONTAL,from_=0, to=800, command = setISO)
isoSlider.pack()

brightnessSlider = Scale(master,label="Brightness", orient=HORIZONTAL,resolution=brightnessSliderRes, from_=-100, to=100, command=setBrightness)
brightnessSlider.pack()

contrastSlider = Scale(master,label="Contrast", orient=HORIZONTAL, resolution= brightnessSliderRes, from_=-100, to=100, command=setContrast)
contrastSlider.pack()

Label(master,text="Exposure Mode").pack()

exposureMode = Entry(master)
exposureMode.pack()

Label(master,text="DRC Mode").pack()
drcMode = Entry(master)
drcMode.pack()


frame = Frame (master,height=600, width=900)
frame.pack()

btn = Button(master, text="Take Picture", command = takePicture)
btn.pack()

btnYuv = Button(master, text="Take YUV Picture", command = takeYuvPicture)
btnYuv.pack()

master.bind("<Configure>", repos)
master.bind("<Return>", mode)
mainloop()

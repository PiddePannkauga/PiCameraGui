from Tkinter import *
from picamera import PiCamera

redAWB = 0.01
blueAWB = 0.01
AWBsliderRes = 0.01
expsliderRes = 0.01
gains = (redAWB,blueAWB)
camera = PiCamera()
camera.awb_mode = 'off'
camera.awb_gains = gains
#camera.exposure_mode = 'off'
camera.vflip = True
camera.start_preview(fullscreen=False,window=(250,250,800,600))

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

def setExposure(val):
    print(val)
    #camera.digital_gain = float(val) 

def setISO(val):
    camera.iso = int(val)


master = Tk()
redSlider = Scale(master,label="RedAWB",resolution=AWBsliderRes, from_=0.0, to=5.0, command=setRed)
redSlider.pack()

blueSlider = Scale(master,label="BlueAWB",resolution=AWBsliderRes, from_=0.0, to=5.0, command=setBlue)
blueSlider.pack()

isoSlider = Scale(master,label="ISO",from_=0, to=800, command = setISO)
isoSlider.pack()

exposureSlider = Scale(master,label="Exposure", resolution=expsliderRes, from_=0, to=1, command=setExposure)
exposureSlider.pack()

btn = Button(master, text="Take Picture", command = takePicture)
btn.pack()


mainloop()



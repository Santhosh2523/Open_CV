import neoapi
import cv2
import sys
import queue
import time

class Baumer:
    def __init__(self, camera,img_queue,parameter):
        self.camera = camera
        self.img_queue = img_queue
        self.parameter = parameter

    def Cam_Connection(self):  #check camera is connected or not
        result = 0
        try:
            camera.Connect()
            print("Camera connected ...")
        except (neoapi.NeoException, Exception) as e:
            print("Camera Connection Error : ", e)
            exit()

    

    def Cam_Parameters(self):  # parameter adjustment
        try:
            if camera.IsConnected() and parameter:
                camera.f.ExposureTime.value = 400  # set exposure value
                print("Exposure Value : ", camera.f.ExposureTime.value)
                print("camera pixel format: ", camera.f.PixelFormat.GetString())
                if not (camera.f.PixelFormat.GetString == "Mono8"):  # pixel format checking and change format
                    camera.f.PixelFormat.value = neoapi.PixelFormat_Mono8
                parameter = False
            else:
                pass
        except (neoapi.NeoException, Exception) as e:
            print("Parameter write Error : ", e)
    
    def Cam_Capture(self):
        try:
            for i in range(0, 10):
                img = camera.GetImage()
                #img.Save(f"test{i}")
                img_queue.put(f"test{i}") 
                time.sleep(0.1)    # Convert to NumPy array for OpenCV
            print("Capture successfully")

        except (neoapi.NeoException, Exception) as exc:
            print(' Capture Error: ', exc)

    def Cam_defect(self,images):
        try:
            for i in images:
                pass
                
        except(neoapi.NeoException,Exception) as exc :
            print('defect checking :' , exc)


parameter = True  # Parameter Loading
img_queue = queue.Queue()   # Create a Queue object
camera = neoapi.Cam()  # attribute
com1 = Baumer(camera,img_queue,parameter) # calling class
com1.Cam_Connection()
com1.Cam_Parameters()
com1.Cam_Capture()
print("Program completed")

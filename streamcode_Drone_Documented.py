
from djitellopy import tello
from djitellopy.tello import BackgroundFrameRead
#Setup tello functions
import cv2
#Need this to use video functions
import time


def main(var):
    var.takeoff()
    #takes off
    inAir = True
    while inAir == True:
        #Repeat streaming while in air, loop streaming
        img = var.get_frame_read().frame
        #Gets the current frame from the drone and assigns it to variable img
        img = cv2.resize(img, (720, 480))
        #resizes the window to bigger size, function takes x and y pixel size
        cv2.imshow("Image", img)
         #shows image in a different window
        cv2.waitKey(1)
        #shows the window for a select amount of time, use this to edit frame rate.

def get_frame_read(self) -> 'BackgroundFrameRead':
    #Need to change the librarys get frame function. Code is sourced from the library
    """Get the BackgroundFrameRead object from the camera drone. Then, you just need to call
    backgroundFrameRead.frame to get the actual frame received by the drone.
    Returns:
        BackgroundFrameRead
    """
    while self.background_frame_read is None:
    #Change the if to while, so the code waits until the video connection starts before continuing.
        address = self.get_udp_video_address()
        self.background_frame_read = BackgroundFrameRead(self, address)  # also sets self.cap
        self.background_frame_read.start()
    return self.background_frame_read


if __name__ == "__main__":
    #Initializes the tello at the beginning of the code
    var = tello.Tello()
    #Sets up a variable for tello
    var.connect()
    #Connects to tello
    var.streamon()
    #Starts the streaming on the tello
    img = var.get_frame_read().frame
    #Gets the current frame from the drone and assigns it to variable img
    img = cv2.resize(img, (720, 480))
    #resizes the window to bigger size, function takes x and y pixel size
    cv2.imshow("Image", img)
    #shows image in a different window
    cv2.waitKey(1)
    main(var)
    #starts main
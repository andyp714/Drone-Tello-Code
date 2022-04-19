
import keyboard
from djitellopy import tello
from djitellopy.tello import BackgroundFrameRead
from threading import Thread
import cv2
import time


def main(var):
    var.takeoff()
    inAir = True
    while inAir == True:
        img = var.get_frame_read().frame
        img = cv2.resize(img, (720, 480))
        cv2.imshow("Image", img)
        cv2.waitKey(1)

def get_frame_read(self) -> 'BackgroundFrameRead':
    """Get the BackgroundFrameRead object from the camera drone. Then, you just need to call
    backgroundFrameRead.frame to get the actual frame received by the drone.
    Returns:
        BackgroundFrameRead
    """
    while self.background_frame_read is None:
        address = self.get_udp_video_address()
        self.background_frame_read = BackgroundFrameRead(self, address)  # also sets self.cap
        self.background_frame_read.start()
    return self.background_frame_read


if __name__ == "__main__":
    var = tello.Tello()
    var.connect()
    var.streamon()
    img = var.get_frame_read().frame
    img = cv2.resize(img, (720, 480))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    main(var)
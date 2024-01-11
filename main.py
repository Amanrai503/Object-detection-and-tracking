import time
import cv2 as cv
import numpy as np
import mss
import detect
from count import *

time.sleep(4)
# link of the game -  https://benbonk.itch.io/crates

# count = enum()  # use if counting

while True:

    with mss.mss() as sct:  # using mss because it is the fastest way to capture screenshots
        screenshot = sct.grab({"top": 830, "left": 335, "width": 1250, "height": 210})
    screenshot = (np.array(screenshot))  # converting to open-cv readable form

    screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)  # converting the image to grayscale. This will make is
    # easier to process. It is optional, and you can skip this part if you have a powerful device (NOTE): BUT MAKE
    # SURE THAT THE NEEDLE IMAGE IS ALSO NOT IN GRAYSCALE

    rect_list = detect(screenshot)  # running the "detect" function present in detect.py
    click_on_match(rect_list, screenshot)  # clicking on the matched points

    # use the following code if counting
    '''
    boxes_ids = count.update(rect_list)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv.putText(screenshot, str(id//2), (x, y - 15), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv.rectangle(screenshot, (x, y), (x + w, y + h), (0, 0, 255), 3)
    '''

    # if "q" is pressed the code will break out of the while loop
    #cv.imshow("counter_window", screenshot)
    key = cv.waitKey(1)
    if key == ord('q'):
        break

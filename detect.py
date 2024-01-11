import cv2 as cv
import numpy as np
import time
import pyautogui
import keyboard
import sys


def detect(ss):
    needle = cv.imread("box.png", cv.IMREAD_GRAYSCALE)  # image which we are looking for in "ss" (NOTE):- use
    # cv.IMREAD_UNCHANGED if you haven't converted the screenshot to grayscale

    result = cv.matchTemplate(ss, needle, cv.TM_SQDIFF_NORMED)  # this will contain all the results from matching
    # source img with needle img

    threshold = 0.12  # increase if not all the objects are being detected

    locations = np.where(result <= threshold)

    locations = list(zip(*locations[::-1]))  # list containing all the co-ordinates of the matches( not grouped )

    needle_w = needle.shape[1]  # width of the needle image
    needle_h = needle.shape[0]  # height of the needle image

    rectangles_list = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
        rectangles_list.append(rect)
        rectangles_list.append(rect)  # list containing all the top-right rectangles i.e. top-right point,height,
        # weight of the matches( not grouped )

    rectangles_list, weights = cv.groupRectangles(rectangles_list, 1, 0.7)  # grouped list of the rectangles

    return rectangles_list


def click_on_match(list_of_grouped_rectangles, ss):
    if len(list_of_grouped_rectangles):

        for (x, y, w, h) in list_of_grouped_rectangles:
            top_left = (x, y)
            bottom_right = (x + w, y + h)

            center_x = x + int(w / 2)
            center_y = y + int(h / 2)
            pyautogui.moveTo(x=(center_x + 335), y=(center_y + 824))
            pyautogui.click()  # clik at the center point of the match

            # cv.rectangle(ss, top_left, bottom_right, color=(0, 255, 0), lineType=cv.LINE_4, thickness=2)  # you can
            # skip this part if you don't want rectangles around the image

# waiting for 0.1 seconds so the system registers the click
            if keyboard.is_pressed('q'):
                sys.exit("you chose to exit")  # exits the code while program while clicking



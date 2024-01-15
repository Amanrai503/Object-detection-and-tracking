# Object-detection-and-tracking
<h2>A simple object detection and tracking program using openCV's temple Template matching (<code>cv2.matchTemplate()</code>)</h2>  

Here is the link of the games i used-
  1) https://benbonk.itch.io/crates
  2) https://www.addictinggames.com/shooting/bowman-2

What you will need is the co-ordinates of top-left corner of the game you want to track and its width and height.
For this you can use- <code><pre>
import pyautogui as py 
import time
while True:
&#160; print(py.position())
&#160; time.sleep(1)  #sleeps for 1 second so your system does not crashes. Press ctrl+c to exit the loop
</code></pre>
pyautogui.position() in a while loop see different position on the screen

Points to keep in mind: -
  1) make sure that bothe the `needle` image and `haystack` image have same channels. What i mean is RGB has 3 channels similaryl RGBA has and grayscale has only one
  2) mone channels means more data to process with results in lowere fps so if you have a low-end device, make sure to change the images to grayscale.
  3) There are different methods of Template Matching. You can play arround and find out which works best for you.  Link of openCV Template Matching methods- https://docs.opencv.org/4.2.0/d4/dc6/tutorial_py_template_matching.html
  4) Different methods will have diffrent threshold valuse. For example- with cv.TM_CCOEFF, 0.9 means a 90% match while with cv.TM_SQDIFF 0.1 means a 90% match. So be careful
  5) If your object is moving to fast then you will need higher fps for counting method to work properly
  6) Use MSS for screenshot as it is faster than Win32 API 
<br>
You can use this code for different purposes. I've attached a few exampls as well (i could not get a good fps in "Example2" because my system is not powerful enough, so its not perfect. But if you have a powerful Device it would work perfectly fine for you)

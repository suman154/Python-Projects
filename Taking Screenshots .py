# program to take screenshot

import pyscreenshot

# to capture the screen
image = pyscreenshot.grab()

# to display the captured image
image.show()

# to save the screenshot
image.save("screenshot.png")
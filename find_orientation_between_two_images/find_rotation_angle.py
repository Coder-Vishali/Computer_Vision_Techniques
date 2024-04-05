from PIL import Image, ImageChops
import numpy as np
import math 
import matplotlib.pyplot as plt
def rmsdiff(x, y):
  """Calculates the root mean square error (RSME) between two images"""
  errors = np.asarray(ImageChops.difference(x, y)) / 255
  return math.sqrt(np.mean(np.square(errors)))
im1 = Image.open(r"e_2.jpg")
# im1.show()
im2 = Image.open(r"e_1.jpg")
# im2.show()
mse = []
for i in range(360):
  im2_rot = im2.rotate(i)
  mse.append(rmsdiff(im1,im2_rot))
print(mse.index(min(mse))) # outputs 90 degrees
plt.plot(mse)
plt.show()
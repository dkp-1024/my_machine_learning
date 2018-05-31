import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
# here we are going to learn how to work on images and generate interesting arrays 
# generating interesting images is a touch task and with the help of images we can easily do this. 
# First, load the image
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = dir_path + "/MarshOrchid.jpg"

# Load the image
image = mpimg.imread(filename)
# You’ll see the output, which is (5528, 3685, 3). 
# This means the image is 5528 pixels high, 3685 pixels wide, and 3 colors “deep”.
# Print out its shape
print(image.shape)

plt.imshow(image)
plt.show()
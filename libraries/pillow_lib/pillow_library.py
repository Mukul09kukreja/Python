# pillow library allows to use image files in python
# Now now i am gonna make a animation files
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
  image = Image.open(arg)
  images.append(image)

images[0].save(
  "costumes.gif", save_all = True, append_images = [images[1]], duration=200, loop=0
)
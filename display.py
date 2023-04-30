import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
def display_image(filename, num_image_to_display=40):
  images = []
  for f in filename:
      try:
        images.append(mpimg.imread(f))
      except Exception as e:
        print(e)

  # NOTE: adjust figsize and columns to view larger/smaller images
  plt.figure(figsize=(40,20))
  columns = 5

  images = images[:num_image_to_display]
  for i, image in enumerate(images):
      plt.subplot(round(len(images) / columns) + 1, columns, i + 1)
      plt.imshow(image)



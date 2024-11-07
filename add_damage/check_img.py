import cv2
import numpy as np
from PIL import Image, ImageDraw
import random
import os

def load_image(path):
    return cv2.imread(path)

# Save image
def save_image(image, filename):
    save_path = os.path.join("./", filename)  # Save to current directory
    cv2.imwrite(save_path, image)
    print(f"Image saved at: {save_path}")

# Run the function
img1_root = "/w/246/daianny00/wikiart/rococo/dmitry-levitzky/valentin-platonovich-musin-pushkin.jpg"
img2_root = "/w/246/daianny00/wikiart_damaged/rococo/dmitry-levitzky/valentin-platonovich-musin-pushkin.jpg"
img1 = load_image(img1_root)
img2 = load_image(img2_root)
save_image(img1, "before.jpg")
save_image(img2, "after.jpg")
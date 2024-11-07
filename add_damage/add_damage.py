import cv2
import numpy as np
from PIL import Image, ImageDraw
import random
import os

# Load image
def load_image(path):
    return cv2.imread(path)

# Save image
def save_image(image, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    cv2.imwrite(path, image)

# Add Gaussian noise
def add_noise(image, mean=0, sigma=25):
    noise = np.random.normal(mean, sigma, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

# Blur effect
def add_blur(image, ksize=(5, 5)):
    return cv2.GaussianBlur(image, ksize, 0)

# Add scratches
def add_scratch(image, num_scratch=5):
    scratch_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(scratch_image)
    for _ in range(num_scratch):
        x1, y1 = random.randint(0, image.shape[1]), random.randint(0, image.shape[0])
        x2, y2 = random.randint(0, image.shape[1]), random.randint(0, image.shape[0])
        draw.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=2)
    return cv2.cvtColor(np.array(scratch_image), cv2.COLOR_RGB2BGR)

# Add stains
def add_stain(image, num_stains=3, radius=30):
    stain_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(stain_image)
    for _ in range(num_stains):
        x, y = random.randint(0, image.shape[1]), random.randint(0, image.shape[0])
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(150, 150, 150, 128))
    return cv2.cvtColor(np.array(stain_image), cv2.COLOR_RGB2BGR)

# Apply multiple damage effects
def add_damage(image_path, output_path):
    image = load_image(image_path)
    image = add_noise(image)
    image = add_blur(image)
    image = add_scratch(image)
    image = add_stain(image)
    save_image(image, output_path)

# Main function to process all images
def process_all_images(input_root, output_root):
    for subdir, _, files in os.walk(input_root):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(subdir, file)
                relative_path = os.path.relpath(input_path, input_root)
                output_path = os.path.join(output_root, relative_path)
                add_damage(input_path, output_path)
                print(f"Processed and saved: {output_path}")

# Run the function
input_root = "/w/246/daianny00/wikiart/rococo/dmitry-levitzky"
output_root = "/w/246/daianny00/wikiart_damaged/rococo/dmitry-levitzky"
process_all_images(input_root, output_root)

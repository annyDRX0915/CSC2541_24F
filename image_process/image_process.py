import os
import random
import argparse
from PIL import Image, ImageDraw

def resize_image(input_path, output_path, resolution=512):
    """Resize image to the specified resolution and save it."""
    img = Image.open(input_path)
    img_resized = img.resize((resolution, resolution), Image.LANCZOS)  # 使用 LANCZOS 替换 ANTIALIAS
    img_resized.save(output_path)
    print(f"Resized image saved to {output_path}")

def generate_mask(resolution=512, mask_ratio=0.3):
    """Generate a random mask for the image with a specified mask ratio."""
    mask = Image.new("L", (resolution, resolution), 255)  # Start with a white mask (no masking)
    draw = ImageDraw.Draw(mask)

    # Calculate mask size based on mask_ratio
    mask_width = int(resolution * random.uniform(mask_ratio / 2, mask_ratio))
    mask_height = int(resolution * random.uniform(mask_ratio / 2, mask_ratio))

    # Generate a random position for the mask
    x = random.randint(0, resolution - mask_width)
    y = random.randint(0, resolution - mask_height)

    # Draw a black rectangle (mask) on the white background
    draw.rectangle([x, y, x + mask_width, y + mask_height], fill=0)
    return mask

def process_images(input_dir, output_dir, resolution=512, mask_ratio=0.3):
    """Process all images in a directory, resizing them and generating corresponding masks."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for img_name in images:
        input_path = os.path.join(input_dir, img_name)
        output_image_path = os.path.join(output_dir, f"resized_{img_name}")
        output_mask_path = os.path.join(output_dir, f"mask_{img_name}")

        # Resize image
        resize_image(input_path, output_image_path, resolution)

        # Generate and save mask
        mask = generate_mask(resolution, mask_ratio)
        mask.save(output_mask_path)
        print(f"Mask saved to {output_mask_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images and generate random masks.")
    parser.add_argument("--input-dir", required=True, help="Directory with input images.")
    parser.add_argument("--output-dir", required=True, help="Directory to save resized images and masks.")
    parser.add_argument("--resolution", type=int, default=512, help="Resolution to resize images to (default: 512).")
    parser.add_argument("--mask-ratio", type=float, default=0.3, help="Ratio of the image to cover with mask (default: 0.3).")

    args = parser.parse_args()

    process_images(args.input_dir, args.output_dir, args.resolution, args.mask_ratio)

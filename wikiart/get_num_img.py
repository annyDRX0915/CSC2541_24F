import os

# Define the path to your main directory
main_directory = '/w/246/daianny00/wikiart/rococo'

# Function to count .jpg files recursively
def count_jpg_files(directory):
    jpg_count = 0
    for root, dirs, files in os.walk(directory):
        jpg_files = [f for f in files if f.lower().endswith('.jpg')]
        jpg_count += len(jpg_files)
    return jpg_count

# Dictionary to store counts
jpg_counts = {}

# Go through each subfolder in the main directory
for subfolder in os.listdir(main_directory):
    subfolder_path = os.path.join(main_directory, subfolder)
    
    # Check if it’s a directory
    if os.path.isdir(subfolder_path):
        # Count .jpg files recursively in the subfolder
        jpg_counts[subfolder] = count_jpg_files(subfolder_path)

# Display the counts for each folder
for folder, count in jpg_counts.items():
    print(f"{folder}: {count} .jpg files")

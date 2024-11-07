import requests
import os
import zipfile

# Define the destination folder for downloads and extraction
destination_folder = "/w/246/daianny00/wikiart"
os.makedirs(destination_folder, exist_ok=True)

# List of file URLs
file_urls = [
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/abstract_expressionism.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/baroque.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/ecole_de_paris.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/expressionism.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/impressionism.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/naive_art_primitivism.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/neo_impressionism.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/neoclassicism.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/post_impressionism.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/pre_raphaelite_brotherhood.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/realism.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/rococo.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/romanticism.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/surrealism.zip",
    "https://github.com/asahi417/wikiart-crawler/releases/download/v0.0.0/symbolism.zip"
]

# Function to download a file
def download_file(url, folder):
    local_filename = os.path.join(folder, url.split("/")[-1])
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(local_filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    print(f"Downloaded {local_filename}")
    return local_filename

# Download each file and save paths to downloaded files
downloaded_files = []
for url in file_urls:
    downloaded_file = download_file(url, destination_folder)
    downloaded_files.append(downloaded_file)

print("All files have been downloaded to:", destination_folder)

# Extract each downloaded ZIP file
for zip_file_path in downloaded_files:
    if zip_file_path.endswith(".zip"):
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(destination_folder)
        print(f"Extracted {zip_file_path} to {destination_folder}")
        # Optionally delete the ZIP file after extraction
        os.remove(zip_file_path)
        print(f"Deleted {zip_file_path}")

print("All files have been extracted to:", destination_folder)
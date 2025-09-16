import os
from pillow_heif import register_heif_opener
from PIL import Image

# Enable HEIC support for Pillow
register_heif_opener()

# Path to your images folder (update this!)
input_folder = "images/Diya"
output_folder = "images/Diya_converted"

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".heic"):
        heic_path = os.path.join(input_folder, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(output_folder, jpg_filename)

        # Open and convert
        image = Image.open(heic_path)
        image.save(jpg_path, "JPEG")
        print(f"Converted: {filename} → {jpg_filename}")

print("✅ Conversion complete! All .HEIC files saved as .jpg")

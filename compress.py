import os
from PIL import Image

def compress_images(
    input_folder,
    output_folder=None,
    quality=60,
    max_width=None,
    max_height=None,
    keep_format=True
):
    """
    Compresses all image files in a folder.

    Parameters:
        input_folder (str): Folder containing images.
        output_folder (str): Optional output folder. If None, images overwrite.
        quality (int): JPEG quality (1-95). Lower = more compression.
        max_width (int): Optional resize max width.
        max_height (int): Optional resize max height.
        keep_format (bool): If True keeps original format, else converts to JPEG.
    """

    if output_folder:
        os.makedirs(output_folder, exist_ok=True)

    supported_ext = [".jpg", ".jpeg", ".png", ".webp"]

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in supported_ext:
                continue

            input_path = os.path.join(root, file)
            rel_path = os.path.relpath(root, input_folder)

            # Output path
            if output_folder:
                out_dir = os.path.join(output_folder, rel_path)
                os.makedirs(out_dir, exist_ok=True)
                output_path = os.path.join(out_dir, file)
            else:
                output_path = input_path

            try:
                img = Image.open(input_path)

                # Optional resizing
                if max_width or max_height:
                    img.thumbnail((max_width or img.width, max_height or img.height))

                # Format handling
                save_format = img.format if keep_format else "JPEG"

                # PNG compression
                if save_format == "PNG":
                    img.save(output_path, optimize=True)
                else:
                    img.save(output_path, optimize=True, quality=quality)

                print(f"Compressed: {input_path} -> {output_path}")

            except Exception as e:
                print(f"Failed: {input_path} ({e})")


if __name__ == "__main__":
    # Example usage
    compress_images(
        input_folder="images/oldcity",
        output_folder="images/oldcity",  # set None to overwrite
        quality=65,
        max_width=1920,
        max_height=1080,
        keep_format=True
    )

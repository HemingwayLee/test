import argparse
import os
from PIL import Image

def resize_images_in_folder(folder_path, target_width=810):
    """
    Resizes images in a folder to a specified width, maintaining aspect ratio.

    Args:
        folder_path (str): The path to the folder containing the images.
        target_width (int, optional): The desired width for the resized images. Defaults to 810.
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.tif')):
            image_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(image_path)
                original_width, original_height = img.size
                aspect_ratio = original_height / original_width
                target_height = int(target_width * aspect_ratio)

                resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS) # Use LANCZOS for best quality.
                resized_img.save(image_path)  # Overwrite the original image
                print(f"Resized: {filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A script to change height with path as arguments")
    parser.add_argument("--path", "-p", help="the folder path contains images")    
    args = parser.parse_args()

    # Example usage:
    if args.path:
        resize_images_in_folder(args.path)
    else:
        print("input your path...")




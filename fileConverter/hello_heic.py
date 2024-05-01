from PIL import Image
import os
import pillow_heif
import numpy as np
import cv2

# from pillow_heif import register_heif_opener

# register_heif_opener()

# folder_path = "/Users/rosemary/Downloads/"

folder_path = "/Users/rosemary/Desktop/"
for filename in os.listdir(folder_path):
  if filename.endswith(".HEIC"):
    input_filepath = os.path.join(folder_path, filename)
    output_filepath = os.path.splitext(input_filepath)[0] + ".jpg"  # Change extension

    try:
      heif_file = pillow_heif.open_heif(input_filepath)
      # image = image.convert('RGB')
      # image.save(output_filepath, quality=95)
      
      np_array = np.asarray(heif_file)
      cv2.imwrite(output_filepath, np_array)
      print(f"Converted {filename} to JPEG")
      os.remove(input_filepath)

    except FileNotFoundError:
      print(f"Error: File {filename} not found.")

print("Finished converting PNGs to JPEGs.")


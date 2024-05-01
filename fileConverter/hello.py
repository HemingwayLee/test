from PIL import Image
import os

folder_path = "/Users/rosemary/Downloads/玉米/"
for filename in os.listdir(folder_path):
  if filename.endswith(".png"):
    input_filepath = os.path.join(folder_path, filename)
    output_filepath = os.path.splitext(input_filepath)[0] + ".jpg"  # Change extension

    try:
      image = Image.open(input_filepath)
      image = image.convert('RGB')
      image.save(output_filepath, quality=95)

      print(f"Converted {filename} to JPEG")
      os.remove(input_filepath)

    except FileNotFoundError:
      print(f"Error: File {filename} not found.")

print("Finished converting PNGs to JPEGs.")


import argparse
from PIL import Image
import os

def main(folder_path):
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



if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="A script to change height with path as arguments")
  parser.add_argument("--path", "-p", help="the folder path contains images")    
  args = parser.parse_args()

  # Example usage:
  if args.path:
    main(args.path)
  else:
    print("input your path...")


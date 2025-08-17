# Don't use this, it is not working...

import argparse
import subprocess
from moviepy.editor import VideoFileClip

def crop_16_9_to_9_16(input_path, output_path):
    try:
        clip = VideoFileClip(input_path)
        original_width, original_height = clip.size
        
        print(f"Original video dimensions: {original_width}x{original_height}")

        new_width = int(original_height * (9 / 16))
        print(f"New video dimensions will be: {new_width}x{original_height}")
       
        command_list = [
            "ffmpeg",
            "-i", f"{input_path}",
            "-vf", f"crop={new_width}:{original_height}:0:0",
            "-c:v", "libx264",
            "-c:a", "aac",
            f"{output_video}"
        ]

        try:
            result = subprocess.run(
                command_list,
                input='y\n',
                check=True,  # Raise an exception if the command fails
                capture_output=True,  # Capture stdout and stderr
                text=True      # Decode output as text
            )

            print("Command executed successfully!")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)

        except subprocess.CalledProcessError as e:
            print(f"An error occurred while executing ffmpeg. Return code: {e.returncode}")
            print("STDOUT:", e.stdout)
            print("STDERR:", e.stderr) 
        
        print(f"Video cropped successfully! Saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# --- Example Usage ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a video into 916 parts.")
    parser.add_argument("--path", "-p", type=str, help="Path to the input MP4 video file.")

    args = parser.parse_args()
    output_video = "my_9_16_video_cropped.mp4"
    
    # NOTE: Ensure 'my_16_9_video.mp4' exists in the same directory.
    # For this example, let's assume it's a 1920x1080 video.
    
    crop_16_9_to_9_16(args.path, output_video)


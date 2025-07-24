from moviepy.editor import VideoFileClip
import os
import argparse

def split_video_into_n_parts(video_path, n_parts, output_dir="output_clips"):
    """
    Splits an MP4 video into N approximately equal parts.

    Args:
        video_path (str): Path to the input MP4 video file.
        n_parts (int): The number of parts to split the video into.
        output_dir (str): Directory to save the output video clips.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    try:
        clip = VideoFileClip(video_path)
    except Exception as e:
        print(f"Error loading video file '{video_path}': {e}")
        return

    duration = clip.duration
    
    # Calculate approximate duration of each part
    part_duration = duration / n_parts

    print(f"\n--- Splitting Video ---")
    print(f"Input Video: {video_path}")
    print(f"Video duration: {duration:.2f} seconds")
    print(f"Splitting into {n_parts} parts, each approx. {part_duration:.2f} seconds")

    for i in range(n_parts):
        start_time = i * part_duration
        # Ensure the last part goes to the very end of the video
        end_time = min((i + 1) * part_duration, duration)

        # Create subclip
        subclip = clip.subclip(start_time, end_time)

        # Define output filename
        base_name = os.path.basename(video_path)
        name, ext = os.path.splitext(base_name)
        # Ensure the extension is .mp4 for consistency, even if input was different
        output_filename = os.path.join(output_dir, f"{name}_part_{i+1}.mp4")

        print(f"Exporting part {i+1}: {start_time:.2f}s to {end_time:.2f}s to {output_filename}")
        try:
            subclip.write_videofile(output_filename, codec="libx264", audio_codec="aac", fps=clip.fps)
        except Exception as e:
            print(f"Error exporting part {i+1} to {output_filename}: {e}")
            # Optionally continue or break based on desired behavior
            continue 

    clip.close()
    print(f"\nVideo split successfully into {n_parts} parts in '{output_dir}'.")
    print("--- Splitting Complete ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split an MP4 video into N parts.")
    parser.add_argument("--path", "-p", type=str, help="Path to the input MP4 video file.")
    parser.add_argument("--parts", "-n", type=int, help="The number of parts to split the video into.")
    parser.add_argument("--output_dir", type=str, default="output_clips",
                        help="Directory to save the output video clips (default: output_clips).")

    args = parser.parse_args()

    # Input validation
    if not os.path.exists(args.path):
        print(f"Error: Input video file not found at '{args.path}'")
    elif not os.path.isfile(args.path):
        print(f"Error: Provided path '{args.path}' is not a file.")
    elif args.parts <= 0:
        print(f"Error: Number of parts (N) must be a positive integer.")
    else:
        split_video_into_n_parts(args.path, args.parts, args.output_dir)


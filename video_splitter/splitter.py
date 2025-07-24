from moviepy.editor import VideoFileClip
import os

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

    clip = VideoFileClip(video_path)
    duration = clip.duration
    
    # Calculate approximate duration of each part
    part_duration = duration / n_parts

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
        output_filename = os.path.join(output_dir, f"{name}_part_{i+1}{ext}")

        print(f"Exporting part {i+1}: {start_time:.2f}s to {end_time:.2f}s to {output_filename}")
        subclip.write_videofile(output_filename, codec="libx264", audio_codec="aac")

    clip.close()
    print(f"Video split successfully into {n_parts} parts in '{output_dir}'.")

# Example Usage:
if __name__ == "__main__":
    input_video = "day2.mp4"  # Replace with your video file path
    num_parts = 3                   # Replace with the desired number of parts

    # Create a dummy video for testing if you don't have one
    # from moviepy.editor import ColorClip, concatenate_videoclips
    # print("Creating a dummy video for demonstration...")
    # clip1 = ColorClip((640, 480), color=(255, 0, 0), duration=5)
    # clip2 = ColorClip((640, 480), color=(0, 255, 0), duration=5)
    # clip3 = ColorClip((640, 480), color=(0, 0, 255), duration=5)
    # final_clip = concatenate_videoclips([clip1, clip2, clip3])
    # final_clip.write_videofile(input_video, fps=24)
    # print(f"Dummy video '{input_video}' created.")

    if os.path.exists(input_video):
        split_video_into_n_parts(input_video, num_parts)
    else:
        print(f"Error: Input video '{input_video}' not found. Please provide a valid path or uncomment the dummy video creation.")


from moviepy.editor import VideoFileClip
import os

def split_video(input_video_path, segment_duration_minutes=3, output_dir="output_segments"):
    """
    Splits a long MP4 video into multiple shorter MP4 videos of a specified duration.

    Args:
        input_video_path (str): The path to the input MP4 video file.
        segment_duration_minutes (int): The desired duration of each segment in minutes.
        output_dir (str): The directory where the output segments will be saved.
    """
    if not os.path.exists(input_video_path):
        print(f"Error: Input video file not found at '{input_video_path}'")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: '{output_dir}'")

    try:
        video = VideoFileClip(input_video_path)
    except Exception as e:
        print(f"Error loading video: {e}")
        return

    duration_seconds = video.duration
    segment_duration_seconds = segment_duration_minutes * 60

    num_segments = int(duration_seconds // segment_duration_seconds)
    if duration_seconds % segment_duration_seconds != 0:
        num_segments += 1

    print(f"Input video duration: {duration_seconds:.2f} seconds")
    print(f"Splitting into {segment_duration_minutes}-minute segments...")

    base_name = os.path.splitext(os.path.basename(input_video_path))[0]

    for i in range(num_segments):
        start_time = i * segment_duration_seconds
        end_time = min((i + 1) * segment_duration_seconds, duration_seconds)

        output_filename = os.path.join(output_dir, f"{base_name}_part_{i+1:03d}.mp4")

        print(f"Processing segment {i+1}/{num_segments}: {start_time:.2f}s to {end_time:.2f}s -> '{output_filename}'")

        try:
            # Use 'libx264' codec for MP4 output, and 'preset' for encoding speed/quality
            # 'crf' (Constant Rate Factor) controls the quality (lower is better, 0-51, 23 is default)
            segment = video.subclip(start_time, end_time)
            segment.write_videofile(
                output_filename,
                codec="libx264",
                audio_codec="aac",
                preset="medium",  # You can try 'fast', 'medium', 'slow'
                ffmpeg_params=["-crf", "23"] # Adjust CRF for quality/size trade-off
            )
            segment.close() # Important to close the subclip to release resources
        except Exception as e:
            print(f"Error processing segment {i+1}: {e}")

    video.close() # Close the main video clip to release resources
    print("Video splitting complete.")

if __name__ == "__main__":
    # --- Configuration ---
    input_video = "/Users/rosemary/Downloads/Tokyo_stree_view_1.mp4"  # <--- IMPORTANT: Change this to your video file
    segment_length = 3                    # Duration of each segment in minutes
    output_directory = "video_segments"   # Directory to save the output videos

    # --- Run the splitter ---
    split_video(input_video, segment_length, output_directory)

    print("\nScript finished. Check the 'video_segments' folder for your split videos.")

